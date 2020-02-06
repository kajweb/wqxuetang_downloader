#!/usr/bin/python3
# -*- coding: UTF-8 -*- 

from utils import *
from wqxtDownloader import *;

# 初始化全局变量
globalvar_init();
# 初始化urllib
setCookiesFile(os.getcwd()+"\\cookies.txt");
initUrllib();
# 初始化logging


if __name__ == '__main__':
	# usage: python3 main.py <book_id> <start> <end>
	loggingLevel("INFO");
	LSArg = len(sys.argv);
	if LSArg==1:
		bid = input("请输入需要下载的bid：");
		book = wqxtDownloader( bid );
		book.start();
	else:
		bid = sys.argv[1];
		book = wqxtDownloader( bid );
		book.start( *(int(x) for x in sys.argv[2:]) );