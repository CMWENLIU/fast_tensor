import gensim
from gensim import corpora, models, similarities
from collections import defaultdict
from pprint import pprint
import os
import Stemmer
import glob
import numpy as np


def stem_restop():
	stopwords = [] 
	stemmer = Stemmer.Stemmer('english')
	#all_files = glob.glob("*.test")
	all_files = os.listdir()
	with open ('/home/xxliu10/bigdata/stopwords.txt', 'r') as stopwordsfile:
		stopwords = [line.strip() for line in stopwordsfile]

	print (len(stopwords))
	print (stopwords[20], stopwords[220])
	for f in all_files:
		with open (f, 'r') as infile:
			newfile = f + '.new'
			with open (newfile, 'w', encoding = 'utf-8') as outfile:
				linelist = []
				for line in infile:
					string = []
					for word in line.split():
						wordnew = stemmer.stemWord(word)
						if wordnew not in stopwords:
							string.append(wordnew)								
					oneline = (' '.join(string))
					linelist.append(oneline)
				outfile.write('\n'.join(linelist))


def build_dic_corpus(workdir):
	os.chdir(workdir)
	all_files = glob.glob('*.txt')
	documents = []	
	for f in all_files:
		with open (f, 'r') as infile:
			for line in infile:
				documents.append(line)
	print(len(documents))
	texts = [[word for word in document.lower().split()] for document in documents]
	frequency = defaultdict(int)
	for text in texts:
		for token in text:
			frequency[token] += 1
	texts = [[token for token in text if frequency[token] > 10] for text in texts]
	#pprint(texts)
	dictionary = corpora.Dictionary(texts)
	dictionary.save('tfidfdic.dict')  # store the dictionary, for future reference
	print(dictionary[0])
	print('The volcabulary size is: ')
	print(len(dictionary))
	'''
	dicpairs = dictionary.token2id
	print (dicpairs)
	count = 0
	with open('dic.txt.dic', 'w', encoding = 'utf-8') as dicfile:
		for w in dicpairs:			
			dicfile.write(str(count) + ' '+ str(w) + '\n')
			count += 1
	#print(dicpairs)
	new_doc = "Human computer interaction human sermon technology  human pc trump eat computer"
	new_vec = dictionary.doc2bow(new_doc.lower().split())
	print(new_vec)
	print(type(new_vec))
	'''
	corpus = [dictionary.doc2bow(text) for text in texts]
	#print(corpus)
	print('The type of corpus')
	print(type(corpus))
	corpora.MmCorpus.serialize('tfidfdic.mm', corpus)  # store to disk, for later use
	#print(corpus)
	tfidf = models.TfidfModel(corpus)
	'''
	vec = [(0, 1), (4, 1), (5, 6), (9, 10)]
	#print(tfidf[vec])
	tfidfofnewvec = tfidf[new_vec]
	print (tfidfofnewvec)
	print (type(tfidfofnewvec[0]))
	print(type(tfidfofnewvec))
	mydic = dict((x, y) for x, y in tfidfofnewvec)
	print (type(mydic))
	print(mydic)
	for key, value in mydic.items():
		print(key, value)
	print (mydic[3380])
	'''
	#---------Following get my tfidf for all documents
	tfresult = np.zeros([len(documents), len(dictionary)], dtype = float)
	label = np.zeros([len(documents)], dtype = int)
	i = 0
	for f in all_files:
		newname = f + '.tfidf'
		with open (newname , 'w', encoding = 'utf-8') as outfile:
			with open (f, 'r') as infile:
				for line in infile:
					myvec = dictionary.doc2bow(line.lower().split())
					thistfidf = tfidf[myvec]
					mydic = dict((x, y) for x, y in thistfidf)
					outfile.write(f[0] + ' ')
					for key, value in mydic.items():
						newkey = key + 1
						outfile.write(str(newkey) + ':' + str(value) + ' ')
						tfresult[i, key] = value
						label[i] = int(f[0])
					outfile.write('\n')
					i += 1
	np.save('result.npy', tfresult)
	np.save('label.npy', label)
	print(tfresult.shape)
	print(label.shape)
	print (i)			

if __name__== '__main__':
	workdir = '/home/xxliu10/bigdata/tfidf/bbc'
	#stem_restop()
	build_dic_corpus(workdir)
