import jieba
import numpy as np
from gensim.models import KeyedVectors
from keras.models import load_model

class Detector():
    
    def __init__(self, pad_len, wv, model):
        jieba.load_userdict('mydict.txt')
        self.wv = KeyedVectors.load(wv, mmap='r')
        self.pad_len = pad_len
        self.model = load_model(model)
        self.response = ['這可能不是文章？', '這聽起來有道理', '這只是主觀意見吧', '這感覺不太可信喔']
        
    def embed(self, text):
        words = jieba.lcut(text)
        vecs = []
        for w in words:
            try:
                vecs.append(self.wv[w])
            except:
                vecs.append(np.zeros(self.wv.vector_size))
        return np.reshape(self.pad(vecs), (-1, self.pad_len, self.wv.vector_size))
        
    def pad(self, words):
        if len(words) > self.pad_len:
            words = words[:self.pad_len]
        elif len(words) < self.pad_len:
            words += [np.zeros(self.wv.vector_size) for i in range(self.pad_len-len(words))]
        return words
    
    def predict(self, text):
        words = self.embed(text)
        res = self.model.predict(words)
        return self.response[np.argmax(res)]