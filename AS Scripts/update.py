import aerospike
from util import Timer

# Configure the client
config = {
  'hosts': [ ('127.0.0.1', 3000) ]
}

# Create a client and connect it to the cluster
try:
  client = aerospike.client(config)
  conn = client.connect()
except:
  import sys
  print("failed to connect to the cluster with", config['hosts'])
  sys.exit(1)


try:
  with Timer() as t:
    for PK in range(10 ** 7):
      # Write a record
      conn.put(('test', 'company', PK), {
        'salary': 15000
      })
  print('Elapsed {:f} seconds'.format(t.secs))
except Exception as e:
  import sys
  print("error: {0}".format(e), sys.stderr)


# Close the connection to the Aerospike cluster
client.close()