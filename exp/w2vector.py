import os
import glob
import numpy as np


def loadGloveModel(gloveFile):
    print ("Loading Glove Model")
    f = open(gloveFile,'r')
    model = {}
    for line in f:
        splitLine = line.split()
        word = splitLine[0]
        embedding = np.array([float(val) for val in splitLine[1:]])
        model[word] = embedding
    print ("Done.",len(model)," words loaded!")
    return model	


def get_datasets(business_data_file, enter_data_file, politics_data_file, sport_data_file, tech_data_file):
    """
    Loads textinline data from files, splits the data into words and generates labels.
    Returns split sentences and labels.
    """
    # Load data from files
    business_examples = list(open(business_data_file, "r").readlines())
    business_examples = [s.strip() for s in business_examples]
    enter_examples = list(open(enter_data_file, "r").readlines())
    enter_examples = [s.strip() for s in enter_examples]
    politics_examples = list(open(politics_data_file, "r").readlines())
    politics_examples = [s.strip() for s in politics_examples]
    sport_examples = list(open(sport_data_file, "r").readlines())
    sport_examples = [s.strip() for s in sport_examples]
    tech_examples = list(open(tech_data_file, "r").readlines())
    tech_examples = [s.strip() for s in tech_examples]

    datasets = dict()
    datasets['data'] = business_examples + enter_examples + politics_examples + sport_examples + tech_examples
    target = [0 for x in business_examples] + [1 for x in enter_examples] + [2 for x in politics_examples] + [3 for x in sport_examples] + [4 for x in tech_examples]
    datasets['target'] = target
    datasets['target_names'] = ['business_examples', 'enter_examples', 'politics_examples', 'sport_examples', 'tech_examples']
    return datasets

def load_data_labels(datasets):
    """
    Load data and labels
    :param datasets:
    :return:
    """
    # Split by words
    x_text = datasets['data']
    x_text = [clean_str(sent) for sent in x_text]
    # Generate labels
    labels = [0, 1, 2, 3, 4]
    print(len(x_text))
    for i in range(len(x_text)):
        label = [0 for j in datasets['target_names']]      
        label[datasets['target'][i]] = labels[i]
        labels.append(label)
    y = np.array(labels)
    return [x_text, y]

def clean_str(string):
    """
    Tokenization/string cleaning for all datasets except for SST.
    Original taken from https://github.com/yoonkim/CNN_sentence/blob/master/process_data.py
    
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
    return string.strip().lower()
    """
    #just return string if already cleaned
    return string

if __name__== '__main__':
	os.chdir('/Users/joy/bigdata/')
	model = loadGloveModel('vec.txt')
	#print (type(model['hello']))
	os.chdir('/Users/joy/bigdata/bbcready/')
	datasets = get_datasets('b.txt', 'e.txt', 'p.txt', 's.txt', 't.txt')
	x_text, y = load_data_labels(datasets)
	print(type(x_text), type(y))
	max_document_length = max([len(x.split(' ')) for x in x_text])
	print (max_document_length)
	print (len(x_text), len(y))
	a = np.zeros(shape=(len(y), max_document_length * 25))
	for index, item in enumerate(x_text):
		linelist = item.split(' ')
		i = 0
		for word in linelist:
			
			if (word not in model):
				emb = [0] * 25	
			else:
				emb = model[word]
			for val in emb:
				a[index][i] = val
				i += 1
	print(x_text[1000])
	print(a[1000])
	np.save(output, a)
	np.save(labels, y)
	print(y[1000])

