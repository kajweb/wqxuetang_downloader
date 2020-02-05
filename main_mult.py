#!/usr/bin/python3
# -*- coding: UTF-8 -*- 

from utils import *
from wqxtDownloader import *;
import logging

# 初始化全局变量
globalvar_init();
# 初始化urllib
setCookiesFile(os.getcwd()+"\\cookies.txt");
initUrllib();
# 初始化logging

def parseMultBid( bids ):
	while len(bids):
		bid = bids.pop(0);
		book = wqxtDownloader( bid );
		book.start();
		logging.info("下载bookid {} 完成".format( str(bid) ));

if __name__ == '__main__':
	# usage: python3 main.py <book_id> <book_id>
	loggingLevel("INFO");
	LSArg = len(sys.argv);
	if LSArg==1:
		bids = input("请输入需要下载的bid(以" "间隔)：");
		Abid = bids.split( " " );
		parseMultBid( Abid );
	else:
		bids = sys.argv[1:];
		parseMultBid( bids );