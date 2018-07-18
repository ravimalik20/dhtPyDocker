import os
from hashlib import sha256

NUM_NODES = 5

for i in range(NUM_NODES):
	name = "node_{}".format(i)
	cmd = "docker container run -d --name {} -e HOSTNAME={} dht".format(name, name)

	os.system(cmd)
