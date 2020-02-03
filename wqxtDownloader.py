#!/usr/bin/python3
# -*- coding: UTF-8 -*- 

from utils import *
from wqxtPDF import *
import json
import logging
import jwt
import socket

class wqxtDownloader():
	fileExt = ".jpg";
	downloadFolder = "books/IMG";
	# sleepRange = {
	# 	"start": 2,
	# 	"end": 5,
	# 	"precision": 1
	# };
	sleepRange = {
		"start": 6,
		"end": 15,
		"precision": 1
	};
	errorConfig = {
		"times": 5,
		"sleep": 1
	}

	# 构造函数
	def __init__( self, bid ):
		# 储存输入列表
		self.bid 	= bid;
		self.jwt_key = self.getJwtKey();
		bookInfo = self.initread();
		self.name = bookInfo['name'];
		self.page = int(bookInfo['pages']);
		self.kData = self.getK();
		folder = self.getFolder();
		self.createFolder( folder );
		self.folder = folder;
		self.catatree = self.getCatatree();
		self.invalidpic = self.getInvalidPicInfo()


	# 获得配置文件的jwt_key
	def getJwtKey( self ):
		conf = getConf();
		jwt_key = conf.get('wqxt', 'jwt_key');
		return jwt_key;

	# 获得下载页面的基础URL
	def getBaseUrl( self, page ):
		return "https://lib-nuanxin.wqxuetang.com/page/img/{}/{}".format( self.bid, str(page) );

	# 初始化阅读书籍
	def initread( self ):
		url = "https://lib-nuanxin.wqxuetang.com/v1/read/initread?bid={}".format( self.bid );
		curl = get_value("urllib");
		request = curl.request.urlopen(url);
		data = request.read().decode("UTF-8");
		bookInfo = json.loads( data );
		pages = bookInfo['data'];
		return pages;
		# data: {
		# 	canread: 1
		# 	upperlimit: 1
		# 	bid: "{BID}"
		# 	toshelf: null
		# 	name: "{书本名称}"
		# 	title: "《书本标题》"
		# 	pages: "页码"
		# 	coverurl: "https://bookask-cover.oss-cn-beijing.aliyuncs.com/c/3/209/{BID}/{BID}.jpg!b"
		# 	volume_list: []
		# 	ismultivolumed: "0"
		# 	lastpage: "1"
		# 	last_volume: "1"
		# 	price: "价格"
		# 	sellprice: "出售价格"
		# 	canreadpages: "可以阅读的数量"
		# 	uid: null
		# 	textbook: "0"
		# }

	# 获得目录
	def getCatatree( self ):
		url 	 = "https://lib-nuanxin.wqxuetang.com/v1/book/catatree?bid={}".format( self.bid );
		curl 	 = get_value("urllib");
		request  = curl.request.urlopen(url);
		data 	 = request.read().decode("UTF-8");
		cataTree = json.loads( data );
		cataTreeData = cataTree['data'];
		# self.parseCatatree( cataTreeData );
		return cataTreeData;


	# 获得书本信息
	def getBookInfo( self ):
		# https://lib-nuanxin.wqxuetang.com/page/size/?bid=
		# {"data":{"bid":"","d":{"w":"524.16","h":"737.28"},"isocr":false},"errcode":0,"errmsg":"success"}
		pass;

	# 获得解密序列
	def getK( self ):
		url 	= "https://lib-nuanxin.wqxuetang.com/v1/read/k?bid={}".format( self.bid );
		curl 	= get_value("urllib");
		request = curl.request.urlopen(url);
		data 	= request.read().decode("UTF-8");
		kInfo 	= json.loads( data );
		kData 	= json.dumps(kInfo['data']);
		return kData;

	def getPageUrl( self, page ):
		baseUrl 	= self.getBaseUrl( page );
		getKparmas 	= self.generateKparmas( page );
		pageUrl = baseUrl + "?k=" + getKparmas;
		return pageUrl;

	def generateKparmas( self, page ):
		jwt_key  = self.jwt_key;
		curTime  = str(int(time.time()));
		time_sq3 = curTime + "000";
		jwt_data = {
			"p": page,
			"t": time_sq3,
			"b": self.bid,
			"w": 1000,
			"k": self.kData,
			"iat": curTime
		};
		jwt_enc = jwt.encode( jwt_data, jwt_key, algorithm='HS256');
		return jwt_enc.decode(encoding='utf-8');

	def start( self, *args ):
		lNumber = len(args);
		if lNumber == 0:
			start = 1;
			end = self.page;
		elif lNumber == 1:
			start = 1;
			end = args[0];
		else:
			start = args[0];
			end = args[1];
		# 计算总页码
		countNum = int(end) - int(start) + 1;
		# 记录当前次数
		downloadTimes = 1;
		# 本次操作的页码列表
		pageLists = [];
		bookName = self.name;
		bid 	 = self.bid;
		logging.info("{}开始下载{}，共 {} 页".format( str(bid), bookName, str(countNum) ));
		for page in range( start, end+1 ):
			url = self.getPageUrl( page );
			path = self.getImgPath( page );
			Errortimes = 0
			while(True):
				try:
					downloadPage = self.downloadImage( url, path );
					pageLists.append( path );
					if downloadPage:
						sleepRange = self.sleepRange;
						ts = getRandom( sleepRange['start'], sleepRange['end'], sleepRange['precision'] );
						logging.info("{}下载成功 第{}页({}/{}) 随机{}s".format( str(bid), page, str(downloadTimes), str(countNum), str(ts) ));
						time.sleep( ts )
					else:
						logging.warning("{}跳过下载 第{}页({}/{})".format( str(bid), page, str(downloadTimes), str(countNum) ));
					downloadTimes += 1;
					break;
				except socket.timeout:
					Errortimes += 1;
					logging.error("{}下载超时 第{}页({}/{}) 正在重试第{}次".format( str(bid), page, str(downloadTimes), str(countNum), str(Errortimes) ));
				except InvalidPictureError:
					Errortimes += 1;
					logging.error("{} 获取到了失败的图片 第{}页({}/{}) 正在重试第{}次".format(str(bid), page, str(downloadTimes), str(countNum), str(Errortimes)));
					self.kData = self.getK(); # 重新获取k
					time.sleep( self.errorConfig['sleep'] )
				if Errortimes > self.errorConfig['times']:
					raise TooManyRetry;
		# PDF
		name 	 = "_".join([ self.name, str(start), str(end) ]);
		catatree = self.catatree;
		pdf 	 = wqxtPDF(  bid, name, catatree );
		pdf.addPages( pageLists );
		pdf.generatePDF();

	def getFolder( self ):
		downloadFolder = self.downloadFolder;
		bid = self.bid;
		folder = "/".join([ downloadFolder, bid ])
		return folder;

	def createFolder( self, folder ):
		mKStatus = mkdir( folder );
		if mKStatus:
			logging.info("成功创建文件夹 {}".format(folder));
		else:
			logging.warning("失败创建文件夹 {}".format(folder));

	def downloadImage( self, url, path ):
		curl = get_value("urllib");
		isExists = os.path.exists(path)
		if not isExists:
			bid = self.bid;
			headers = {
				"referer": "https://lib-nuanxin.wqxuetang.com/read/pdf/{}".format(bid),
				"tips":		"Brother...... Working late at night...???"
			};
			requestPer = curl.request.Request(url=url, headers=headers);
			request = curl.request.urlopen(requestPer, timeout=10);
			data = request.read()
			compareNBytes = 10000;
			if data[0:compareNBytes] == self.invalidpic[0:compareNBytes]:
				raise InvalidPictureError
			f = open(path,"wb")
			f.write(data)  
			f.close()
			return True;
		else:
			return False;

	def getImgPath( self, page ):
		fileExt = self.fileExt;
		folder 	= self.folder;
		path = "{folder}/{page}{fileExt}".format( folder=folder, page=str(page), fileExt=fileExt );
		return path;

	def getInvalidPicInfo(self):
			f = open('invalid_pic.jpg','rb');
			invalidpic = f.read()
			f.close()
			return invalidpic;

class InvalidPictureError(Exception):
	pass;

class TooManyRetry(Exception):
	def __init__(self):
		logging.critical("重试次数过多，程序终止，请尝试重新执行main.py");