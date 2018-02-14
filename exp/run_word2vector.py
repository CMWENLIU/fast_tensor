from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
sentences = LineSentence('/home/xxliu10/repos/gensim/gensim/models/data.txt')
#sentences = [["cat", "say", "meow"], ["dog", "say", "woof"]]
model = Word2Vec(sentences, size=20, window=5, min_count=1, workers=4)
say_vector = model['say']  # get vector for word
print(say_vector, len(say_vector))
