#! /usr/bin/env python
import os
import glob
import codecs
import uuid
import string
import random 


def create_unistring():
  size = 0
  with open('uniwords.uni', 'r') as f:
    size = sum(1 for _ in f)  
  with open('uniString.uni', 'w', encoding = 'utf-8') as outf:
    lines_seen = set()
    count = 0
    for x in range(0, size):
      myword = random_generator(12, "abcdefghijklmnopqrstuvwxyz")
      if myword not in lines_seen: # not a duplicate 
        lines_seen.add(myword)
        outf.write(myword + '\n')
      else:
          count += 1
  print('There are ' + str(count) + ' duplicate in created string')

    


def get_uni_word():
	lines_seen = set() # holds lines already seen
	with open('uniwords.uni', 'w', encoding = 'utf-8') as wtfile:
		count = 0
		for line in open('all_words.all', 'r'):
			if line not in lines_seen: # not a duplicate
				wtfile.write(line)
				lines_seen.add(line)
			else:
				count += 1
		print ('There are: ' + str(count) + ' lines have duplicate')
	dic_size = sum(1 for line in open('uniwords.uni'))
	print ('Dicitonary size is : ' + str(dic_size))
	return dic_size			

def roundnumbers():
	with open('00.txt','r') as inf:
		with open('allwords.txt', 'w', encoding = 'utf-8') as outf:
			count = 0
			for line in inf:
				for word in line.split():
					number  = float(word)
					number2 = (round(number,6))
					count += 1
					if count % 100:
						outf.write(str(number2) + ' ')
					else:
						outf.write(str(number2) + '\n')


def get_all_words(): #get all words from files, then put to new files and all_words.all
	all_txt_files = glob.glob("*.txt")
	with open ('all_words.all', 'w', encoding = 'utf-8') as outfile:
		for f in all_txt_files:
			with open(f, 'r') as infile:   
				for line in infile:
					for word in line.split():
						outfile.write(word + '\n')

def random_generator(size=7, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for x in range(size))						
						


def writemytxt():
	all_txt_files = glob.glob("*.txt")
	
	#keylist = [line.rstrip('\n') for line in open('uniwords.uni')]
	keylist = []
	valuelist = []
	with open('uniwords.uni') as f:
		keylist = f.readlines()
		#you may also want to remove whitespace characters like `\n` at the end of each line
		keylist = [x.strip() for x in keylist] 
	#valuelist = [line.rstrip('\n') for line in open('uniString.uni')]
	with open('uniString.uni') as f:
		valuelist = f.readlines()
		valuelist = [x.strip() for x in valuelist]
	print (keylist[2])
	print (valuelist[2])
	dic = dict( zip( keylist, valuelist))
	for f in all_txt_files:		
		with open (f, 'r') as infile:
			outfname = f + '.ready'
			with open (outfname, 'w', encoding = 'utf-8') as outfile:
				linelist = []				
				for line in infile:						
					string = []
					for x in line.split():							
						word = dic[x]
						string.append(word)
					oneline = (' '.join(string))
					linelist.append(oneline)
				outfile.write('\n'.join(linelist))
						#some_list = ['abc-123', 'def-456', 'ghi-789', 'abc-456']
						#if any("abc" in s for s in some_list):

def myGlove():
	count = 0
	with open ('myglove.glove', 'w', encoding = 'utf-8')	as outfile:
		with open ('uniwords.uni', 'r') as uniembedding:
			with open ('uniString.uni', 'r') as unistring:
				uni_embedding = [line.strip() for line in uniembedding]
				uni_string = [line.strip() for line in unistring]
				for i in uni_string:
					line = i + ' ' + uni_embedding[count]
					count += 1
					outfile.write(line + '\n')

def readFiles():
	os.chdir('/home/xxliu10/bigdata/tweets/download/')
	with open ('myglove.txt', 'r') as infile:
		for line in infile:
			print (line)

if __name__== '__main__':
  workdir = '/home/xxliu10/bigdata/fromdbn/7000ready'
  #embed_size = 25
  #sen_length = 280
  os.chdir(workdir)
  #get_all_words()
  #get_uni_word()
  #create_unistring()
  #writemytxt()	
  myGlove()	
	#replacechar()
	#roundnumbers()
	#remove_dup()
	#createunistring()
	#convertEmbedding()
	#writemytxt()

	#readandwrite("test")
	#test('test')
