from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
'''
sentences = LineSentence('/home/xxliu10/bigdata/data.txt')

#sentences = [["cat", "say", "meow"], ["dog", "say", "woof"]]
model_20 = Word2Vec(sentences, size=20, window=5, min_count=1, workers=4)
model_20.save('w2v_20')
model_80 = Word2Vec(sentences, size=80, window=5, min_count=1, workers=4)
model_80.save('w2v_80')

model_200 = Word2Vec(sentences, size=200, window=5, min_count=1, workers=4)
model_200.save('/home/xxliu10/bigdata/w2v_200')
print('finished')
'''
model = Word2Vec.load('/home/xxliu10/bigdata/w2v_200')
vector = model['obama']  # get vector for word
print(say_vector, len(say_vector))


