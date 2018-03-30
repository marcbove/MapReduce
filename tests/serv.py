'''
Basic remote example sending ask messages. SERVER
@author: Daniel Barcelona Pons
'''
from pyactor.context import set_context, create_host, serve_forever
import re
import time
import argparse
import collections
import unicodedata
import pprint

class Count(object):
    _tell = ['wordCount']
    _ask = ['countingWords']

    def __init__(self):
        dictionary = {}

    def countingWords(self, text):
        text = text.lower()
        text = text.decode('unicode-escape')
        text = unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore')
        words = re.findall('\w+', str(text))
        return len(words)

    def wordCount(self, text):
        #text = text.lower()
        text = text.decode('unicode-escape')
        text = unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore')
        words = re.findall('\w+', str(text))
        word = filter(lambda x: x.isalnum(), words)
        if dictionary.has_key(word):
            dictionary[word] += 1 
        else:
            dictionary[word]= 1
        pprint.pprint(dictionary.items())

if __name__ == "__main__":
    set_context()
    host = create_host('http://127.0.0.1:1277/')

    e1 = host.spawn('echo1', Count)
    serve_forever()
