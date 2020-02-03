#!/usr/bin/python
# -*- coding: UTF-8 -*- 

import configparser
import urllib.request
import os
import sys
import requests
import logging
import random

def getUA():
    UA = [
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;",
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 OPR/65.0.3467.78",
        "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
        "Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
        "Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10",
        "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11"
    ];
    return random.choice(UA)

def getConf():
    confFile = "conf.ini";
    conf = configparser.ConfigParser();
    conf.read( confFile );
    return conf;

def initUrllibNoCookies():
    opener = urllib.request.build_opener()
    UA = getUA();
    headers=("User-Agent", UA);
    opener.addheaders=[headers];
    urllib.request.install_opener(opener);
    set_value("urllib",urllib);

def mkdir( folder ):
    isExists = os.path.exists(folder)
    if not isExists:
        os.makedirs( folder, 0o777 );
        return True;
    return False;

def getRandom( start, end, precision=0 ):
    num = random.uniform( start, end );
    if precision == 0:
        return int(num);
    return round( num , precision );

def loggingLevel( level=logging.info ):
    if level == "CRITICAL":
        _level = logging.CRITICAL;
    elif level == "ERROR":
        _level = logging.ERROR;
    elif level == "WARNING":
        _level = logging.WARNING;
    elif level == "INFO":
        _level = logging.INFO;
    else:
        _level = logging.DEBUG;
    logging.basicConfig(stream=sys.stderr, format='%(asctime)s [%(levelname)s] %(message)s', level=_level);



def globalvar_init():
    global _global_dict
    _global_dict = {}

def set_value(name, value):
    _global_dict[name] = value

def get_value(name, defValue=None):
    try:
        return _global_dict[name]
    except KeyError:
        return defValue