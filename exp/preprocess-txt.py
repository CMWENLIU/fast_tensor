import gensim
from gensim import corpora, models, similarities
from collections import defaultdict
from pprint import pprint
import os
import glob
import numpy as np
import csv
import time
import re

from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
import nltk as nk

def clean_str(string):
    
    #remove url link
    string = re.sub(r"http\S+", "", string)
    #remove @user or #topic in tweets
    string = re.sub(r'(?:^|\s)[@#].*?(?=[,;:.!?]|\s|$)', r'', string)
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
    #string =''.join([i for i in string if not i.isdigit()])
	#Remove punctuation
    #string =re.sub('[^A-Za-z0-9]+', ' ', string)
    #Remove extra spaces and change to lowercase
    string = string.strip().lower()
    #Remove backslashes in string
    string = string.replace('\\', '')
    #string = re.sub(' +', ' ', string)
    return string

def stem_restop(inputstr):
	words = word_tokenize(inputstr)
	stopwords = open("stopwords.txt").readlines()
	stopwords = [item.strip() for item in stopwords]
	ps = PorterStemmer()
	result = []
	line = ''
	for word in words:
		new = ps.stem(word)
		if new not in stopwords:
			result.append(new)								
		line = (' '.join(result))
	print(inputstr)
	print(line)
	return line

if __name__== '__main__':
	#nk.download('punkt')
	stem_restop('Hello this is a working are you works above from this lines of talking Hello this is a working are you works above from this lines of talking Hello this is a working are you works above from this lines of talking')
