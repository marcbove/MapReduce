from pyactor.context import set_context, create_host, serve_forever


def create_host_port():
  port = 6001
  while True:
    try:
      return create_host('http://127.0.0.1:{}/'.format(port))
    except Exception as e:
      print(e)
      port += 1


if __name__ == '__main__':
  PORT = 6001

  set_context()

  host = create_host_port()

  registry = host.lookup_url('http://127.0.0.1:6000/regis', 'Registry', 'registry')

  name = 'host' + str(len(registry.get_all()))

  registry.bind(name, host)

  pprint.pprint(registry.get_all())

  print('host listening at port {}'.format(PORT))

  serve_forever()