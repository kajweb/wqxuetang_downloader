#!/usr/bin/python3
# -*- coding: UTF-8 -*- 

from utils import *
import copy
import os
import img2pdf
import time
import fitz # pip3 install pymupdf

class wqxtPDF():
	fileExt = ".pdf"
	imgExt  = ".jpg" 
	PDFFolder = "books/PDF";
	PDFTempFolder = "books/temp";
	lists = [];
	filePath = None;
	tempPath = None;


	def __init__( self, bid, name,lNumber, start ,end, bookmarks=[], lists=lists):
		self.bid = bid;
		self.name = name;
		self.lNumber = lNumber
		self.start = start
		self.end = end
		self.lists = lists;
		self.bookmarks = bookmarks;
		mkdir(self.PDFFolder);
		mkdir(self.PDFTempFolder);
		[tempPath, filePath] = self.getFilePath();
		self.tempPath = tempPath
		self.filePath = filePath;

	def getFilePath( self ):
		if self.filePath:
			return self.filePath;
		else:
			curTime = int(time.time());
			PDFFolder	= self.PDFFolder;
			PDFTempFolder	= self.PDFTempFolder;
			bid			= self.bid;
			name 		= self.name;
			fileExt 	= self.fileExt;
			fileName = "{}_{}_{}{}".format( bid, name, curTime, fileExt );
			tempName = "{}_{}_{}_nomarks{}".format( bid, name, curTime, fileExt );
			tempNamePath = "/".join([ PDFTempFolder, tempName ]);
			fileNamePath = "/".join([ PDFFolder, fileName ]);
			return ([ tempNamePath, fileNamePath ]);

	def addPage( self, filename ):
		self.lists.append( filename );

	def addPages( self, filesLists ):
		self.lists += filesLists;

	def generatePDF( self ):
		tempPath = self.tempPath;
		filePath = self.filePath;
		lists = self.lists;
		logging.info("生成pdf文件中");
		pfn_bytes = img2pdf.convert( lists, with_pdfrw=False );
		with open( tempPath, "wb" ) as f:
			f.write(pfn_bytes);
			f.close();
		logging.info("向pdf写入目录中");
		self.addBookMarks();
		logging.info("【pdf路径】：\n{}".format(  os.path.abspath(filePath) ));

	def addBookMarks( self ):
		tempPath = self.tempPath;
		filePath = self.filePath;
		doc = fitz.open( tempPath );
		toc = doc.getToC();
		self.tocAppend( toc, self.bookmarks );
		new_toc = self.toc_checker(toc)
		doc.setToC(new_toc);
		doc.save( filePath );
		doc.close();
		os.remove( tempPath )

	def tocAppend( self, toc, lists ):
		for chapter in lists:
			level = int(chapter['level']);
			label = chapter['label'];
			pnum = int(chapter['pnum']);
			toc.append([ level, label, pnum ]);
			if "children" in chapter.keys():
				self.tocAppend( toc, chapter['children'] );

	def toc_checker(self, toc_origin):
		if self.lNumber == 0:
			return toc_origin
		elif self.lNumber == 1:
			new_toc = []
			for title in toc_origin:
				if title[2] > self.end: break
				new_toc.append(title)
		else :
			new_toc = []
			for i,title in enumerate(toc_origin):
				if title[2] > self.end: break
				if title[0] == 1:
					current_lv1 = i
				if title[2] in range(self.start,self.end+1):
					new_toc.append(title)
					new_toc[-1][2] -= self.start
			temp_toc = copy.deepcopy(toc_origin[current_lv1])
			temp_toc[2] = 1
			new_toc = [temp_toc] + new_toc
		return new_toc