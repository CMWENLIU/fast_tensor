#! /usr/bin/env python
import os
import re
import glob
import codecs




def remove_line_break(foldername):
	os.chdir(foldername)
	allfiles = glob.glob("*.txt")
	with open ('1.tech', 'w', encoding = 'utf-8') as write:
		for file in allfiles:
			with open(file, 'r') as read:
				lines = read.readlines()
				mystr = '\t'.join([line.strip() for line in lines])
				
				#Original taken from https://github.com/yoonkim/CNN_sentence/blob/master/process_data.py
				string = re.sub(r"[^A-Za-z0-9(),!?\'\`]", " ", mystr)
				string = re.sub(r"\'s", " \'s", string)
				string = re.sub(r"\'ve", " \'ve", string)
				string = re.sub(r"n\'t", " n\'t", string)
				string = re.sub(r"\'re", " \'re", string)
				string = re.sub(r"\'d", " \'d", string)
				string = re.sub(r"\'ll", " \'ll", string)
				string = re.sub(r",", " , ", string)
				string = re.sub(r"!", " ! ", string)
				string = re.sub(r"\(", " \( ", string)
				string = re.sub(r"\)", " \) ", string)
				string = re.sub(r"\?", " \? ", string)
				string = re.sub(r"\s{2,}", " ", string)
				string = string.strip().lower()
				write.write(string + '\n')

if __name__== '__main__':
	foldername = 'test/'
	remove_line_break(foldername)
	#readandwrite("test")
	#test('test')