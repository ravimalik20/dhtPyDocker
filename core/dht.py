import hashlib, os
from core.storage.core import StorageEngine
from socket import socket, AF_INET, SOCK_STREAM, gethostname
from threading import Thread

DHT_PORT = 4567

class DHTNode:
	def __init__(self, name):
		self.name = name
		self.id = self.__hash(name)
		self.hostname = os.environ['HOSTNAME']
		self.pred_hostname, self.succ_hostname = "", ""
		self.storage = StorageEngine()
		
		self.__join_ring()

		print ("Hostname: {}".format(self.hostname))

		print ("Pred_hostname: {} Succ_hostname: {}".format(self.pred_hostname,
			self.succ_hostname))

	def get(self, key):
		if self.__isOwner(key):
			return self.storage.get(key)
		else:
			# forward to successor
			pass

	def put(self, key, value):
		if self.__isOwner(key):
			return self.storage.put(key, value)
		else:
			# forward to successor
			pass

	def __join_ring(self):
		i_node = int(self.name.split("_")[1])

		self.succ_hostname = "node_{}".format( ((i_node+1) % 5) )
		self.pred_hostname = "node_{}".format( ((i_node-1) % 5) )

	def __hash(self, key):
		key = key.encode("utf-8")
		return hashlib.sha256(key).hexdigest()

	def __isOwner(self, key):
		return True

	def __str__(self):
		val = "Name:{}\nID:{}".format(self.name, self.id)
		return val

class DHTServerWorker(Thread):
	def __init__(self):
		Thread.__init__(self)

		self.sock = socket(AF_INET, SOCK_STREAM)
		self.sock.bind((gethostname(), DHT_PORT))

		print ("Bound to {}".format(gethostname()))

		self.dht = DHTNode(os.environ['HOSTNAME'])

	def run(self):
		self.sock.listen()

		while True:
			(c_sock, c_add) = self.sock.accept()
			message = self.sock.recv(1024).decode()

			print (message)

class DHT:
	def __init__(self):
		self.master_name = "node_0"
		self.master_id = self.__hash(self.master_name)
		self.master_hostname = "node_0"

	def start(self):
		self.server = DHTServerWorker()
		self.server.start()

	def __hash(self, key):
		key = key.encode("utf-8")
		return hashlib.sha256(key).hexdigest()
