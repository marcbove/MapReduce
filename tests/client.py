from pyactor.context import set_context, create_host, Host, sleep, shutdown
from pyactor.exceptions import TimeoutError
import sys
import re
import unicodedata

class Server(object):
    _ask = {'countingWords'}
    _tell = []

    def countingWords(self, text):
        text = text.lower()
        text = text.decode('unicode-escape')
        text = unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore')
        words = re.findall('\w+', str(text))
        return len(words)


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
    res2 = server.countingWords(file2.read())
    
    print('{} words'.format(res))
    print('{} words'.format(res2))

    print('Total words = {}'.format(res+res2))
    
    file.close()
    file2.close()

    shutdown()