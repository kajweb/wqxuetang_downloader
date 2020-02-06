from utils import *
import json;
import logging;

class wqxtLoader():
	commonError = "未定义的错误信息，请提交下一行到issues：https://github.com/kajweb/wqxuetang_downloader/issues";

	def isRegistered( self, mobile ):
		url = "http://open.izhixue.cn/mobile";
		postData = {
			"mobile": mobile,
			"area_code": 86,
			"type": 5
		};
		request = post( url, postData );
		data = request.read().decode("UTF-8");
		isRegistered = json.loads( data );
		code = isRegistered['code'];
		if code == "20619":
			# 手机号已存在
			return True;
		elif code == "0":
			# 手机号不存在
			logging.error( "手机号码不存在：{}".format(mobile) );
			return False;
		else:
			logging.critical( self.commonError );
			logging.info( isRegistered );

	def sendSms( self, mobile ):
		url = "http://open.izhixue.cn/sms";
		postData = {
			"phone": mobile,
			"area_code": 86,
			"type": 5
		};
		request = post( url, postData );
		data = request.read().decode("UTF-8");
		isSend = json.loads( data );
		sendCode = isSend['code'];
		if sendCode == "0":
			# 发送成功
			return True;
		elif sendCode == "20901":
			# 发送失败
			logging.error( "发送信息失败，原因：{}".format(isSend['message']) );
			return False;
		else:
			logging.critical( self.commonError );
			logging.info( isSend );

	def loginBySms( self, mobile, code ):
		url = "http://open.izhixue.cn/mobile_login?response_type=code&client_id=wqxuetang&redirect_uri=https%3A%2F%2Fwww.wqxuetang.com%2Fv1%2Flogin%2Fcallbackwq&scope=userinfo&state=https%3A%2F%2Flib-nuanxin.wqxuetang.com%2F%23%2F";
		postData = {
			"mobile": mobile,
			"area_code": 86,
			"code": code
		};
		request = post( url, postData );
		data = request.read().decode("UTF-8");
		isSend = json.loads( data );
		# TODO