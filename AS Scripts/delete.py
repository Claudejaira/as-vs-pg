import aerospike
from util import Timer

# Configuração para conectar
config = {
  'hosts': [ ('127.0.0.1', 3000) ]
}

try:
  client = aerospike.client(config) # prepara cliente
  conn = client.connect() # cria conexão
except:
  import sys
  print("failed to connect to the cluster with", config['hosts'])
  sys.exit(1)


try:
  with Timer() as t:
    for PK in range(10 ** 7):
      # remove a key passada
      conn.remove(('test', 'company', PK))

  print('Elapsed {:f} seconds'.format(t.secs))
except Exception as e:
  import sys
  print("error: {0}".format(e), sys.stderr)


# Close the connection to the Aerospike cluster
client.close()