#! /usr/bin/env python

import os
import glob
import codecs
import re
						
def clean_str(string):
    """
    Tokenization/string cleaning for all datasets except for SST.
    Original taken from https://github.com/yoonkim/CNN_sentence/blob/master/process_data.py
    """
    string = re.sub(r"[^A-Za-z0-9(),!?\'\`]", " ", string)
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
	#Added to remove digits
    string =''.join([i for i in string if not i.isdigit()])
	#Remove punctuation
    string =re.sub('[^A-Za-z0-9]+', ' ', string)
    #Remove extra spaces
    string = string.strip().lower()
    string = re.sub(' +', ' ', string)
    return string
			
def readandwrite(filefolder):
	allfiles = glob.glob("*.txt")
	with open ('training.one', 'w', encoding = 'utf-8') as writefile:
		lines_seen = set()
		for f in allfiles:
			with open(f, 'r', errors='ignore') as readtxt:
				lines = readtxt.readlines()
				#change multiple lines of text file to one string
				mystr = '\t'.join([line.strip() for line in lines])
				if f.contain('business')				
string = clean_str(mystr)
else if f.
				#get string between 40 and 400 words, remove duplicats
				if 40 < length < 400 and string not in lines_seen:
					writefile.write(string + '\n')
					lines_seen.add(string)
				
if __name__== '__main__':
	filefolder = "/home/xxliu10/repo/artificial-news-agent/datasets/raw_data/bbc/politics")
	os.chdir(filefolder)
	#test('test')
