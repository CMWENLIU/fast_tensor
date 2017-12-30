#Convert documents into vector representation(or say big matrix)

import tensorflow as tf
# Load Google's pre-trained Word2Vec model.
# model = gensim.models.Word2Vec.load_word2vec_format('./datasets/tweets_word2vec_pretrained_models/GoogleNews-vectors-negative300.bin', binary=True)
import numpy as np
from operator import add
import glob
import os

#Read pretrained model from local file into python build in dictionary w2v
class readw2vdic:
    def __init__(self,pm_name,pm_path):
        self.name = pm_name
        self.path = pm_path

    # Convert w2v model into python dictionary{word:vector}
    def getw2vdic(self):
        w2v = {}
        if self.name =="bbc_twitter":
            print("loading model {0} ... ...".format(self.name))
            with open(self.path,'r',encoding='utf8') as file:
                for line in file:
                    w2v.update({line.split()[0]: np.array(line.split()[1:])})
            file.close()
            return w2v
        else:
            print("Unknown pretrained model")
            return 0

"""
#Padding sentences to the same length by using self defined symbols, such as 'UNK'.
#This operation will sure each input batch of deep learning model has the same and proper format.
class padding:
    def __init__(self,docpath):
        self.path = docpath

    def pad(self,paddingword):
        # 'paddingword' is the symbol used to pad the sentences.
        unk = ' ' + paddingword
        # Calculate the max length of the input sentences
        with open(self.path, 'r') as file:
            max_len = len(max(file, key=len).split())
            print("The longest sentences is [{0}]".format(max(file, key=len)),"\n its length is ",max_len)
        file.close()
        # Pad short sentences with 'unk'
        with open(self.path, 'r') as old, open('2-1.txt', 'w') as new:
            for line in old:
                diff = max_len - len(line.split())
                new.writelines(line.strip('\n') + diff * unk + '\n')
        old.close()
        new.close()

"""
# Convert training or testing input documents into 3d matrices
class convertd2v:
    def __init__(self,w2vmodel):
        # w2vmodel should be a dictionary containing a {string:np.array} like lookup table
        self.model = w2vmodel
        self.dim = len(next(iter(self.model.values())))

    # If some words not in the dictionary, give a proper solution here. Coming soon.
    def fit(self, X, y):
        return self

    #infile is the absoulate path of the target pure txt file you want to process
    def convert(self, infile):
        with open(infile, 'r',encoding='utf8') as fin:
            train_set = []*self.dim
            # print(self.dim)
            tmp_list = []
            for line in fin.readlines():
                # print(line+"\n")
                vec_mean = [0]*self.dim
                for word in line.split():
                    # print("word in line=====>\n",word)
                    if word in iter(self.model.keys()):
                        tmp_vec = self.model[word]
                        # print(tmp_vec.shape)
                    else:
                        tmp_vec = np.array(np.zeros(self.dim))
                    tmp_vec = tmp_vec.astype(np.float)
                    vec_mean = np.add(vec_mean,tmp_vec)
                    # print("vec_mean......",vec_mean)
                vec_mean = [x/len(line.split()) for x in vec_mean]
                # print(vec_mean)
                tmp_list.append(vec_mean)
            train_set = np.vstack(tmp_list)
        # np.save('./output',train_set)
        fin.close()
        return train_set
#Till now, the above code generate the mean of each tweet(we assume each tweet is a single line...)
if __name__ == '__main__':
    # glove.twitter.27B.100d.txt is the pre trained word2vec model of 100 dimensions.
    # "bbc_twitter"  is a constant, don't need to be changed here.
    # readw2vdic("bbc_twitter",filepath)
    rw2v = readw2vdic("bbc_twitter",'glovetwitter//glove.twitter.27B.50d.txt')
    dic = rw2v.getw2vdic()
    cd2v = convertd2v(dic)
    #file under current directory ended with ".txt" is the input file needed
    # to be convert into input matrix of deep learning model.
    for file in glob.glob("*.txt"):
        print(".......", file, ".......")
        d_matrix = cd2v.convert(file)
        np.save(file,d_matrix)
        print(file, "is processed")

