#! /usr/bin/env python
import os
import glob
import codecs


def remove_dup():
	lines_seen = set() # holds lines already seen
	with open('tech_2.txt', 'w', encoding = 'utf-8') as wtfile:
		for line in open('tech.txt', 'r'):
			if line not in lines_seen: # not a duplicate
				wtfile.write(line)
				lines_seen.add(line)

if __name__== '__main__':
	os.chdir('test/')
	remove_dup()
	#readandwrite("test")
	#test('test')