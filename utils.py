#!/usr/bin/python
# -*- coding: UTF-8 -*- 

import configparser
import urllib.request
import os
import requests
import logging

def getConf():
    confFile = "conf.ini";
    conf = configparser.ConfigParser();
    conf.read( confFile );
    return conf;

def initUrllibNoCookies():
    opener = urllib.request.build_opener()
    headers=("User-Agent","Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 OPR/65.0.3467.78")
    opener.addheaders=[headers]
    urllib.request.install_opener(opener)
    set_value("urllib",urllib);

def mkdir( folder ):
    isExists = os.path.exists(folder)
    if not isExists:
        os.makedirs( folder, 0o777 );
        return True;
    return False;

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