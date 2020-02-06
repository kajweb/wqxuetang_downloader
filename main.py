#!/usr/bin/python3
# -*- coding: UTF-8 -*- 

import sys, getopt

from utils import *
from wqxtDownloader import *;

# 初始化全局变量
globalvar_init();
# 初始化urllib
setCookiesFile(os.getcwd()+"\\cookies.txt");
initUrllib();
# 初始化logging

def parseMultBid( bids ):
	while len(bids):
		bid = bids.pop(0);
		try:
			book = wqxtDownloader( bid );
		except BIDError:
			continue
		book.start([]);
		logging.info("下载bookid {} 完成".format( str(bid) ));


if __name__ == '__main__':
	loggingLevel("INFO");
	try:
		opts, args = getopt.getopt(sys.argv[1:],"hb:p:",["help","books=","pages="])
	except getopt.GetoptError:
		print("main.py -b <BooksID_1>,<BooksID_2> ... [-p <start_page>,<end_page>][-p <end_page>], 或使用-h, --help来获取帮助")
	if opts[0][0] in ['-h','--help']:
		print("用法：python main.py -b <BooksID_1>,<BooksID_2> ... [-p <start_page>,<end_page>][-p <end_page>]\n")
		print("参数：\n")
		print("    -h, --help 查看此帮助\n" )
		print("    -b, --books 后接你要下载的图书BID，支持多个图书，用英文逗号\",\"隔开\n" )
		print("    -p, --pages (可选)后接要下载的页码，从开始到结束<start_page>,<end_page>，中间用英文逗号隔开若只输入一个页码则被认为是结束页码，不输入则下载整本书，若下载多本图书该参数无效\n")
		sys.exit()
	elif opts[0][0] in ['-b', '--books']:
		books_str = opts[0][1].strip()
		books = books_str.split(",")
	if len(books) == 1:
		bid = books[0];
		book = wqxtDownloader( bid );
		if len(opts) > 1:
			pages = opts[1][1].strip()
			book.start(pages.split(','));
		else:
			book.start([]);
	else:
		logging.info("下载多个书目，指定页码被忽略，若要指定页码下载请只下载一个书目");
		parseMultBid(books)

