#! /usr/bin/env python
import os
import glob
import codecs
import uuid
import string
import random 
import re



def remove_substring(): 
	with open ('out.txt', 'w', encoding = 'utf-8') as outfile:
		with open('in.txt', 'r') as infile:
			summ = 0
			count = 0
			for line in infile:
				line = line.split('acc')[1]
				line = line.split(',')[0]
				outfile.write(line + '\n')
				summ += float(line)
				count += 1
			print('The sum of them is: ' + str(summ))
			print('Total instences is: ' + str(count))
			print('The ave of them is: ' + str(summ/count))
					
def writeshellcode():
	train= 'nohup ./svm_multiclass_learn -c parameter rbm630/train_number.dat rbm630/model_number_parameter &'
	test = 'nohup ./svm_multiclass_classify rbm630/test_number.dat rbm630/model_number_parameter rbm630/predictions_number_parameter > rbm630/fold_number_parameter_result.out &'
	with open ('temp_te.txt', 'w', encoding = 'utf-8') as outfile:
		for i in range(1):
			num = 500
			for x in range(0, 50):
				outfile.write(test.replace('number', str(i)).replace('parameter', str(num)) + '\n')
				num += 500


def getmax_fromfile(location):
	os.chdir(location)
	allfiles = glob.glob('*result.out')
	with open ('sum.one', 'w', encoding = 'utf-8') as outf:
		outf.write('10-folds  Accuracy%(Best) Accuracy%(Worst) \n')
		summ = 0
		summmax = 0
		for i in range(1):
			minnum = 100
			maxnum = 0
			keystring = 'fold_' + str(i) + '_'
			for file in allfiles:
				if keystring in file:
					with open(file) as infile:
						lines = infile.readlines()
						ele = re.findall("\d+\.\d+", lines[4])
						outf.write(ele[0] + '\n')
						if minnum >= float(ele[0]):
							minnum = float(ele[0])
						if maxnum <= float(ele[0]):
							maxnum = float(ele[0])
			outf.write(str(i) + ':         ' + str(round((100 - minnum), 2)) + '          ' + str(round((100 - maxnum), 2)) + '\n')
			summ += minnum
			summmax += maxnum
		outf.write('Ave:       ' + str(round((100 - summ), 2)) + '          ' + str(round((100 - summmax), 2)) + '\n')

def writeshellscript():
	with open('tempfilenames.txt', 'w', encoding = 'utf-8') as outfile:
		for i in range(10):
			outfile.write('mv test_' + str(i) + ' set_' + str(i) + '\n')


if __name__== '__main__':
	
	folders = ['/Users/joy/Downloads/set_rbm']
	for f in folders:
		getmax_fromfile(f)
	
	#writeshellcode()
	#writeshellscript()