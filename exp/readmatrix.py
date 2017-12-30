#! /usr/bin/env python
import os
import glob
import codecs
import uuid
import string
import random 


def remove_dup():
	lines_seen = set() # holds lines already seen
	with open('uniEmbedding.txt', 'w', encoding = 'utf-8') as wtfile:
		count = 0
		for line in open('allembedding.txt', 'r'):
			if line not in lines_seen: # not a duplicate
				wtfile.write(line)
				lines_seen.add(line)
			else:
				count += 1
				print (count)
			

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

#Following remove ',' and round numbers 
def convertEmbedding():
	with open('business_through_dbn.txt', 'r') as infile:
		with open('b.txt', 'w', encoding = 'utf-8') as outfile:
			count = 0
			for line in infile:
				newline = line.replace(',', ' ')
				for word in newline.split():
					number  = float(word)
					#number2 = (round(number,3))
					count += 1
					if count % 100:
						outfile.write(str(number) + ' ')
					else:
						outfile.write(str(number) + '\n')

def random_generator(size=7, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for x in range(size))						
						
def createunistring():
	with open('uniString111.txt', 'w', encoding = 'utf-8') as outf:
		for x in range(0, 8889):
			#myword = uuid.uuid4().hex[:9].upper()
			myword = random_generator(8, "abcdefghijklmnopqrstuvwxyz")
			outf.write(myword + '\n')

def writemytxt():
	count = 0
	with open ('tech.txt', 'w', encoding = 'utf-8') as outfile:
		with open ('t.txt', 'r') as infile:
			with open ('uniEmbedding.txt', 'r') as uniembedding:
				with open ('uniString.txt', 'r') as unistring:
					in_file = [line.strip() for line in infile]
					uni_embedding = [line.strip() for line in uniembedding]
					uni_string = [line.strip() for line in unistring]
					for everyword in in_file:
						word = uni_string[uni_embedding.index(everyword)]
						count += 1
						if count % 15:
							outfile.write(word + ' ')
						else:
							outfile.write(word + '\n')
						print (str(count) + '---finished')
						#some_list = ['abc-123', 'def-456', 'ghi-789', 'abc-456']
						#if any("abc" in s for s in some_list):

def myGlove():
	count = 0
	with open ('myglove-3.txt', 'w', encoding = 'utf-8')	as outfile:
		with open ('uniEmbedding.txt', 'r') as uniembedding:
			with open ('uniString.txt', 'r') as unistring:
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
	os.chdir('test/')
	#replacechar()
	#roundnumbers()
	#remove_dup()
	#createunistring()
	#convertEmbedding()
	#writemytxt()
	#myGlove()
	#readandwrite("test")
	#test('test')
