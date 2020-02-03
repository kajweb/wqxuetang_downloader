#!/usr/bin/python3
# -*- coding: UTF-8 -*- 

from utils import *
from wqxtDownloader import *;
import logging

# 初始化全局变量
globalvar_init();
# 初始化urllib
initUrllibNoCookies();
# 初始化logging


if __name__ == '__main__':
	# usage: python3 main.py <book_id> <start> <end>
	loggingLevel("info");
	bid = sys.argv[1];
	book = wqxtDownloader( bid );
	book.start( *(int(x) for x in sys.argv[2:]) );