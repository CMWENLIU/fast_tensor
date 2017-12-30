#! /usr/bin/env python
import os
from TwitterSearch import *
import csv
import time
import re

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

#define the search function
def SearchTweets(searchkey, round):
    try:
        tso = TwitterSearchOrder()  # create a TwitterSearchOrder object
        tso.set_keywords([searchkey])  # let's define all words we would like to have a look for
        tso.set_language('en')  # we want to see German tweets only
        tso.set_include_entities(False)  # and don't give us all those entity information
		
        # it's about time to create a TwitterSearch object with our secret tokens
        ts = TwitterSearch(
            consumer_key='sToxW29MQSeHNGMHkLJd4upux',
            consumer_secret='5BbJoy8pRx3WvvI5zZD09YFpHmUaXiPl2AoNCSCPqS37oVKEI1',
            access_token='798172108010508288-ZKwC04JG1BaT65BhFyi792yA7HadGIK',
            access_token_secret='nEDYhL7NNzXpaJgwtgJJ9ipJMrLm2IqUwNJJY0Xk6Yc2P'
        )
        filename = searchkey + '_' +  str(round)
        fieldnames = ['user', 'tweet', 'time', 'cleantweet']
        with open('%s_tweets.csv' % filename, 'w', encoding="utf-8", newline='') as csvWfile:
            writer = csv.DictWriter(csvWfile, fieldnames=fieldnames)
            writer.writeheader()
            # this is where the fun actually starts :)
            for tweet in ts.search_tweets_iterable(tso):
                cleaned = clean_str(tweet['text'])
                if cleaned[:3] == 'rt ':
                    cleaned = cleaned[3:]
                if len(cleaned) > 20:
                    writer.writerow({'user': tweet['user']['screen_name'], 'tweet': tweet['text'], 'time': tweet['created_at'], 'cleantweet': cleaned})
    except TwitterSearchException as e:  # take care of all those ugly errors if there are some
           print(e)

#defind the keywords for cotegories
keylist = []
with open('keywords.txt') as csvRfile:
    keylist = [line.strip() for line in csvRfile]
index = 264
os.chdir('/home/xxliu10/bigdata/tweets/download/')
while(index < 700):
     for word in keylist:
        SearchTweets(word, index)
        time.sleep(1200)
     index += 1
