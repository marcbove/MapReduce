import sys, pprint

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print 'bad arguments'
    exit()

  dictionary = {}
  path = sys.argv[1]
  with open(path, 'r') as file:
  	for line in file:
  		for word in line.split():
  			word = filter(lambda x: x.isalnum(), word)
	  		if dictionary.has_key(word):
	  			dictionary[word] += 1 
	  		else:
	  			dictionary[word]= 1

  pprint.pprint(dictionary.items())
  print "Nombre paraules", len(dictionary)
  