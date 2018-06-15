from pyactor.context import set_context, create_host, Host, sleep, shutdown, sys, serve_forever
from pyactor.exceptions import TimeoutError
import collections, os, time, re, sys, unicodedata

class Server(object):
	_ask = {'partFile'}
	_tell = ['main', 'init']
	_ref = ['main', 'init']

	def init(self, host):
		remote_host_0 = host.lookup_url('http://192.168.1.46:4321/', Host)
		self.map_0 = remote_host_0.spawn('map_0','host/Map') 
		remote_host_1 = host.lookup_url('http://192.168.1.46:4322/', Host)
		self.map_1 = remote_host_1.spawn('map_1','host/Map') 
		remote_host_2 = host.lookup_url('http://192.168.1.46:4323/', Host)   
		self.map_2 = remote_host_2.spawn('map_2','host/Map')

		self.reducer = host.spawn('reducer', 'host/Reducer') 

	def partFile(self, path, parts):
		with open(path, 'r') as file:
			# Read file
			lines = [line for line in file.readlines() if line != '\n']
			# Create output directory if doesn't exists
			if not os.path.exists('temp'):
				os.makedirs('temp')
			# Partition the file in N parts and save each one in .txt files
			name = path.split('/')[-1][:-4]
			size = len(lines) / parts
			rest = len(lines) % parts
			pivot = 0
			for i in range(parts):
				offset = size + int(i < rest)
				with open('./temp/{}_{}.txt'.format(name, i+1), 'w') as o_file:
					o_file.writelines(lines[pivot:pivot + offset])
				pivot += offset 

	def main(self, txt_0, txt_1, txt_2, function):
		start_t = time.time()
		#self.partFile(txt, 3)
		if function == 'wordCount':
			self.map_0.wordCount(txt_0, self.reducer, start_t)
			self.map_1.wordCount(txt_1, self.reducer, start_t)
			self.map_2.wordCount(txt_2, self.reducer, start_t) 
		elif function == 'countWords':
			self.map_0.countWords(txt_0, self.reducer, start_t)
			self.map_1.countWords(txt_1, self.reducer, start_t)
			self.map_2.countWords(txt_2, self.reducer, start_t) 
		

class Map(object):
	_ask = {'findWords'}
	_tell = ['countWords', 'wordCount']
	_ref = ['countWords', 'wordCount']
	
	def findWords(self, text):
		text = text.lower()
		translator = str.maketrans(dict.fromkeys(string.punctuation))
		text = text.translate(translator)
		text = unicodedata.normalize('NFD', text)
		text = text.encode('ascii', 'ignore')
		text = text.decode('utf-8')
		return re.findall('\w+', str(text))
		
	def wordCount(self, text, reducer, time_t):
		text = text.lower()
		text = re.findall('\w+', str(text))
		reducer.wordCount(collections.Counter(text), time_t)

	def countWords(self, text, reducer, time_t):
		text = text.lower()
		text = re.findall('\w+', str(text))
		reducer.countWords(len(text), time_t)


class Reducer(object):
	_ask = {''}
	_tell = ['countWords','wordCount']

	def __init__(self):
		self.num_words = 0
		self.dictionary = collections.Counter()
		self.num_maps = 3

	def countWords(self, words, time_t):
		self.num_maps = self.num_maps-1
		self.num_words += words
		if (self.num_maps == 0):
			value = (time.time() - time_t)
			with open('.//countWords_result.txt', 'w') as f:
				f.write('There are {} words'.format(self.num_words))
			print('There are {} words'.format(self.num_words))
			print(time.time() - time_t) 

	def wordCount(self, dictionary, time_t):
		self.num_maps = self.num_maps-1
		self.dictionary = self.dictionary + collections.Counter(dictionary)
		if (self.num_maps == 0):
			with open('.//wordCount_result.txt', 'w') as f:
				for e in dictionary:
					f.write(e + ', ' + str(dictionary[e]) + '\n')
			print(dictionary)
			print(time.time() - time_t)

def parseArgs():
	parser = argparse.ArgumentParser()
	egroup = parser.add_mutually_exclusive_group(required=True)
	egroup.add_argument('-C', '--counting-words', action='store_true',
					  help='outputs the total number of words in FILE')
	egroup.add_argument('-W', '--word-count', action='store_true',
					  help='outputs the occurrences of each word in FILE')
	parser.add_argument('FILE', help='input file', type=argparse.FileType('r'))
	return parser.parse_args()


if __name__ == "__main__":
	set_context()
	host = create_host('http://192.168.1.46:4320')

	server = host.spawn('server', 'host/Server')
	server.init(host)

	#args = parseArgs()
	file_name = raw_input('\nInsert file name:')
	function = raw_input('Escoge opcion:\n\t- countWords\n\t- wordCount')
	
	#if inp == 'countWords':
	#	function = 'countWords'
	#if inp == 'wordCount':
	#	function = 'wordCount'
	file = '{}_{}.txt'.format(file_name, 0)
	with open('./{}'.format(file)) as f:
		os.system("wget http://0.0.0.0:8000/{}".format(file))
		txt_0 = f.read()

	file = '{}_{}.txt'.format(file_name, 1)
	with open('./{}'.format(file)) as f:
		os.system("wget http://0.0.0.0:8000/{}".format(file))
		txt_1 = f.read()

	file = '{}_{}.txt'.format(file_name, 2)
	with open('./{}'.format(file)) as f:
		os.system("wget http://0.0.0.0:8000/{}".format(file))
		txt_2 = f.read()
	
	server.main(txt_0, txt_1, txt_2, function)

	serve_forever()