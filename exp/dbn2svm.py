import os
import glob
import numpy as np



'''
def npy2text(filefolder):
  os.chdir(filefolder)
  allfiles = glob.glob("*.npy")
  for file in allfiles:    
    x = np.load(file) # Common trained data
    print(x.shape) # output is n*500's numpy array
    print(x[0])
    print(len(x))
    filename = file + '.txt'
    np.savetxt(filename, x, fmt='%10.8f')

npy2text('/home/xxliu10/bigdata/500d')
# y = np.load("bbc_tweets_tfidf_dic.npy").tolist()# Now y is a standard python dictionary
#dic = dict({"word1":4,"word2":5})
#x1 = dic.keys()
#x2 = dic.values()
#x1 ,x2 are all iterable python standard variables

#word = "word1"
#with open("xxx.txt",'r') as f:
#    for line in f.readlines():
#        for word in line.strip().split():
#            if word in dic:
#                print(dic[word])
#float(dic[word])
'''
#np.loadtxt("xx.txt",dtype=float,delimiter=',')
def npy2svm(filefolder):
	os.chdir(filefolder)
	allfiles = glob.glob("*.npy")
	for file in allfiles:
		newname = file + '.txt'
		x = np.load(file)
		with open(newname, 'w', encoding = 'utf-8') as wfile:
			for i in x:
				if 'b_t' in file:
					wfile.write('1 ')
				if 'e_t' in file:
					wfile.write('2 ')
				if 'p_t' in file:
					wfile.write('3 ')
				if 's_t' in file:
					wfile.write('4 ')
				if 't_t' in file:
					wfile.write('5 ')
				count = 1
				for j in i:
					wfile.write(str(count) + ':' + str(j) + ' ')
					count += 1
				wfile.write('\n')
	mergefiles = glob.glob('*.txt')
	'''
	for i in range (10):
		trfiles1 = '_tr_'
		trfiles2 = 'concat' + str(i)
		tefiles1 = '_te_'
		tefiles2 = 'concat' + str(i)
		train = 'train_' + str(i) + '.dat'
		test = 'test_' + str(i) + '.dat'

		with open(train, 'w', encoding = 'utf-8') as outfile:
			for f in mergefiles:
				if trfiles1 in f and trfiles2 in f:
					with open(f, 'r') as infile:
						for line in infile:
							outfile.write(line)
		with open(test, 'w', encoding = 'utf-8') as outfile:
			for f in mergefiles:
				if tefiles1 in f and tefiles2 in f:
					with open(f, 'r') as infile:
						for line in infile:
							outfile.write(line)
	'''
	#following is only for one fold solution:


	trfiles = '_tr_'
	tefiles = '_te_'
	with open('train.dat', 'w', encoding = 'utf-8') as outfile:
		for f in mergefiles:
			if trfiles in f:
				with open (f, 'r') as infile:
					for line in infile:
						outfile.write(line)
	with open('test.dat', 'w', encoding = 'utf-8') as outfile:
		for f in mergefiles:
			if tefiles in f:
				with open (f, 'r') as infile:
					for line in infile:
						outfile.write(line)	

folders = ['/Users/joy/Downloads/rbm1130']

for folder in folders:
	npy2svm(folder)