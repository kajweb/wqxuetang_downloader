#!/usr/bin/python3
# -*- coding: UTF-8 -*- 

from utils import *
import os
import img2pdf
import time

class wqxtPDF():
	fileExt = ".pdf"
	imgExt  = ".jpg" 
	PDFFolder = "books/PDF";
	lists = [];


	def __init__( self, bid, name, lists=lists ):
		self.bid = bid;
		self.name = name;
		self.lists = lists;
		mkdir(self.PDFFolder);

	def getFilePath( self ):
		curTime = int(time.time());
		PDFFolder	= self.PDFFolder;
		bid			= self.bid;
		name 		= self.name;
		fileExt 	= self.fileExt;
		fileName = "{}_{}_{}{}".format( bid, name, curTime, fileExt );
		return "/".join([ PDFFolder, fileName ]);

	def addPage( self, filename ):
		self.lists.append( filename );

	def addPages( self, filesLists ):
		self.lists += filesLists;

	def generatePDF( self ):
		filePath = self.getFilePath();
		lists = self.lists;
		logging.info("生成pdf文件中");
		pfn_bytes = img2pdf.convert( lists, with_pdfrw=False );
		with open( filePath, "wb" ) as f:
			f.write(pfn_bytes);
			f.close();
		logging.info("【pdf路径】：\n{}".format(  os.path.abspath(filePath) ));