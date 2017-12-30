#! /usr/bin/env python

from gensim import corpora
from gensim import utils
from gensim import corpora, models, similarities
from nltk.corpus import stopwords
import preprocessor as p
from collections import Counter
import codecs
import string
import os
import csv
import re
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
from six import iteritems
from gensim import corpora
dataFolder = 'data/'
inputFolder = 'input/'
outputFolder = 'output/'
articlesFolder = 'articles/'

def VisitingFolder(FolderName):
    os.chdir(FolderName)

def CleanData(filenames, target):
    for item in filenames:
        with open(item, 'r', encoding='utf-8') as csvReadfile:
             reader = csv.DictReader(csvReadfile)
             for row in reader:
                newtext = p.clean(row['tweet'])
                newtext1 = re.sub(r'W+', '', newtext)
                finalt = row['tweet'].replace('https://', '')
                #finalt = row['tweet']
                if len(finalt) > 40:
                    target.writerow({'user': row['user'], 'text': finalt, 'length': len(finalt)})
def get_file_list():
    filenames = os.listdir(os.getcwd())
    return filenames

def WriteAllTxt2Single(folderName, writer):
    VisitingFolder(folderName)
    filenames = os.listdir(os.getcwd())
    for item in filenames:
        with codecs.open(item, 'rb') as txtReadfile:
             reader = txtReadfile.readline()
             writer.write(reader + '\n'.encode('ascii'))
        txtReadfile.close()
    os.chdir('..')
def Sumlines(document):
    return sum(1 for line in open(document))

def Mergedocument(folderName, newfile):
    document = []
    VisitingFolder(folderName)
    filenames = os.listdir(os.getcwd())
    for item in filenames:
        with open(item, 'r') as txtReadfile:
             reader = txtReadfile.read()
             document.append(reader)
    txtReadfile.close()
    with open(newfile, 'w') as txtWritefile:
        for line in document:
            txtWritefile.writelines(line + '\n')
    txtWritefile.close()
    print(Sumlines(newfile))
    os.chdir('..')
def Totalwords(doc):
    with open(doc, 'r') as txtReadfile:
        words = [word for line in txtReadfile for word in line.split()]
        print (len(words))

def BuildDoc(docs):
    with open(docs, 'r') as txtReadfile:
        doc = [line.strip() for line in txtReadfile]
    txtReadfile.close()
    return doc

def Dictionry():
    # remove common words and tokenize
    documents = BuildDoc('single.txt')
    stoplist = BuildDoc('stopwords.txt')

    texts = [[word for word in document.lower().split() if word not in stoplist] for document in documents]

    # remove words that appear only once
    from collections import defaultdict
    frequency = defaultdict(int)
    for text in texts:
        for token in text:
            frequency[token] += 1
    texts = [[token for token in text if frequency[token] > 1] for text in texts]
    from pprint import pprint  # pretty-printer
    pprint(texts)
    print (len(texts[0]))
    dictionary = corpora.Dictionary(texts)
    dictionary.save('dic.dict')  # store the dictionary, for future reference
    #print(dictionary)
    corpus = [dictionary.doc2bow(text) for text in texts]
    corpora.MmCorpus.serialize('corpus.mm', corpus)
    print(corpus)

def Transform():
    dictionary = corpora.Dictionary.load('dic.dict')
    corpus = corpora.MmCorpus('corpus.mm')
    tfidf = models.TfidfModel(corpus)
    corpus_tfidf = tfidf[corpus]
    corpora.BleiCorpus.serialize('corpus.lda-c', corpus)
    #for doc in corpus_tfidf:
    #   print(doc)

def Callmodel():
    corpus = corpora.MmCorpus('corpus.mm')
    dictionary = corpora.Dictionary.load('dic.dict')
    lda = models.LdaModel(corpus, id2word=dictionary, num_topics=150)
    lda.print_topics(150)
#################Followint are function calls:

# Mergedocument(articlesFolder, 'single.txt')
'''
with codecs.open('single.txt', 'wb') as txtWritefile:
     WriteAllTxt2Single(inputFolder, txtWritefile)
txtWritefile.close()
print (Sumlines('single.txt'))
'''
VisitingFolder('test/')
with open('test' + '.txt', 'w', encoding='utf-8') as txtWrite:
    with open ('economy_73_tweets.csv', 'r', encoding='utf-8') as csvRead:
        reader = csv.DictReader(csvRead)
        for row in reader:
            text = (row['text'])
            if len(text) > 40:
             txtWrite.write(text + '\n')