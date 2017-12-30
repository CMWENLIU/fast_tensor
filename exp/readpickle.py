import pickle
import os

def read_pickle():
	with open('vocabulary.pickle', 'rb') as handle:
		with open('vocabulary.txt', 'w', encoding = 'utf-8') as wf:	
			obj = pickle.load(handle)
			for line in obj:
				wf.write(line)


#if __name__== '__main__':
workdir = '/home/sheep/bigdata/pickle'
os.chdir(workdir)
read_pickle()
