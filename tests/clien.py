''' 
Basic remote example sending ask messages. CLIENT
@author: Daniel Barcelona Pons
'''
from pyactor.context import set_context, create_host, shutdown
import re
import time
import argparse
import collections
import unicodedata

if __name__ == "__main__":
    set_context()
    host = create_host('http://127.0.0.1:1679')

    e1 = host.lookup_url('http://127.0.0.1:1277/echo1', 'Count', 's2_server')

    res = e1.countingWords('Hi there!, Whats up with your life?')
    print('{} words'.format(res))

    res = e1.wordCount(e1.wordCount('Hi there!, Whats up with your life? Hi there!, Whats up with your life? Hi there!, Whats up with your life?'))
    res = [[key, value] for key, value in res.items()]
    res.sort(key=lambda x: x[1], reverse=True)
    print('; '.join([e[0] + ', ' + str(e[1]) for e in res]))

    shutdown()
