import numpy as np
import os
import glob



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

npy2text('/home/xxliu10/bigdata/fromdbn/test_set_for_cnn/7000')
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

#np.loadtxt("xx.txt",dtype=float,delimiter=',')

