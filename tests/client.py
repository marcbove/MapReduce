from pyactor.context import set_context, create_host, Host, sleep, shutdown
from pyactor.exceptions import TimeoutError
import sys
import re
import unicodedata
import collections

class Server(object):
    _ask = {'countingWords', 'wordCount'}
    _tell = []

    def countingWords(self, text):
        text = text.lower()
        text = text.decode('unicode-escape')
        text = unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore')
        words = re.findall('\w+', str(text))
        print '-----------'
        return len(words)

    def wordCount(self, text):
        text = text.lower()
        text = text.decode('unicode-escape')
        text = unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore')
        words = re.findall('\w+', str(text))
        print words
        print '-------------------------------------------------'
        print collections.Counter(words)
        return collections.Counter(words)


if __name__ == "__main__":
    set_context()
    host = create_host('http://127.0.0.1:1679')
    host2 = create_host('http://127.0.0.1:1680')

    remote_host = host.lookup_url('http://127.0.0.1:1277/', Host)
    print remote_host
    server = remote_host.spawn('server', 'client/Server')

    remote_host2 = host2.lookup_url('http://127.0.0.1:1278/', Host)
    print remote_host2
    server2 = remote_host2.spawn('server', 'client/Server')

    file = open(str(sys.argv[1]), 'r')
    file2 = open(str(sys.argv[2]), 'r')

    res = server.countingWords(file.read())
    res2 = server2.countingWords(file2.read())
    
    print('{} words'.format(res))
    print('{} words'.format(res2))

    print('Total words = {}'.format(res+res2))
    
    res = server.wordCount(file.read())
    res = [[key, value] for key, value in res.items()]
    res.sort(key=lambda x: x[1], reverse=True)
    res2 = server2.wordCount(file2.read())
    res2 = [[key, value] for key, value in res.items()]
    res2.sort(key=lambda x: x[1], reverse=True)

    print('; '.join([e[0] + ', ' + str(e[1]) for e in res]))
    print('; '.join([e[0] + ', ' + str(e[1]) for e in res2]))

    file.close()
    file2.close()

    shutdown()