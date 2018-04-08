import SimpleHTTPServer
import SocketServer
import os
import thread


def startServer():
  PORT = 8000

  web_dir = os.path.join(os.path.dirname(__file__), 'web')
  os.chdir(web_dir)

  Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
  httpd = SocketServer.TCPServer(('', PORT), Handler)
  print('serving at port {}'.format(PORT))
  print(web_dir)
  httpd.serve_forever()
  print('hey')


if __name__ == '__main__':
  thread.start_new_thread(startServer, ())
  print('hi')
