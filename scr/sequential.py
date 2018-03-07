import sys


if __name__ == "__main__":
  if len(sys.argv) != 2:
    print 'bad arguments'
    exit()

  path = sys.argv[2]

  file = open(path, 'r')

  