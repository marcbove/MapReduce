#!/usr/bin/python

import argparse, re, collections, unicodedata


def parseArgs():
  parser = argparse.ArgumentParser()
  group = parser.add_mutually_exclusive_group(required=True)
  group.add_argument('-C', '--counting-words', help='outputs the total number of words in FILE', action='store_true')
  group.add_argument('-W', '--word-count', help='outputs the number of occurrences of each word in FILE', action='store_true')
  parser.add_argument('-b', '--benchmark', help='logs the execution time', action='store_true')
  parser.add_argument('FILE', help='input file', type=argparse.FileType('r'))
  return parser.parse_args()


def countingWords(text):
  text = text.lower()
  text = unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore')
  words = re.findall('\w+', str(text))
  return len(words)


def wordCount(text):
  text = text.lower()
  text = unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore')
  words = re.findall('\w+', str(text))
  return collections.Counter(words)


if __name__ == '__main__':
  args = parseArgs()

  text = args.FILE.read()
  args.FILE.close()
  
  time_taken = 0

  if args.counting_words:
    res = countingWords(text)
    print('{} words'.format(res))
  
  if args.word_count:
    res = wordCount(text)
    res = [[key, value] for key, value in res.items()]
    res.sort(key=lambda x: x[1], reverse=True)
    print('; '.join([e[0] + ', ' + str(e[1]) for e in res]))

  if args.benchmark:
    print('Time taken {:.2f}s'.format(time_taken))
