import os
import collections
import math
import json


class TFIDF:
    def __init__(self, inp_doc, docs):
        self.__tf = {word: self.tf(word, inp_doc) for word in inp_doc}
        if os.path.exists('idf_file.js'):
            with open('idf_file.js', 'r') as idf:
                self.__idf = json.load(idf)
        else:
            self.__idf = {word: self.idf(word, docs) for doc in docs for word in doc}
            with open('idf_file.js', 'w') as idfout:
                json.dump(self.__idf, idfout)

    def tf(self, word, doc):
        return collections.Counter(doc).get(word)/len(doc)

    def idf(self, word, docs):
        docs_c = 0
        for doc in docs:
            if word in doc:
                docs_c += 1
        return math.log(len(docs)/docs_c)

    def tf_idf(self, words):
        result = dict()
        for word in words:
            _tf = self.tf(word, words)
            try:
                _idf = self.__idf[word]
            except KeyError:
                _idf = 0
            result[word] = _tf*_idf
        return result
