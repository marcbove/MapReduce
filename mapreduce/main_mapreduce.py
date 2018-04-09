import SimpleHTTPServer
import SocketServer
import threading
import os


class HttpServer(threading.Thread):
  def run(self, PORT=8000):
    os.chdir(os.getcwd() + '//temp')
    Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
    httpd = SocketServer.TCPServer(('', PORT), Handler)
    print('serving at port {}'.format(PORT))
    httpd.serve_forever()


def partFile(path, parts):
  with open(path, 'r') as file:
    # Read file
    lines = [line for line in file.readlines() if line != '\n']
    # Create output directory if doesn't exists
    if not os.path.exists('temp'): os.makedirs('temp')
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


if __name__ == '__main__':
  partFile('../resources/small.txt', 5)
  HttpServer().start()
