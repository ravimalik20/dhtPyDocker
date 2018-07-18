import hashlib
from core.storage.core import StorageEngine
from socket import socket, AF_INET, SOCK_STREAM, gethostname
import logging
from threading import Thread

DHT_PORT = 4567

class DHTNode:
	def __init__(self, name):
		self.name = name
		self.id = self.__hash(name)
		self.hostname = gethostname()

		self.pred_port, self.succ_port = 0, 0

		self.storage = StorageEngine()

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

	def run(self):
		self.sock.listen()

		while True:
			(c_sock, c_add) = self.sock.accept()
			message = self.sock.recv(1024).decode()

			print (message)

class DHT:
	def __init__(self):
		self.master_name = "node_0"
		self.master_id = hashlib.sha256(self.master_name.encode("utf-8")).hexdigest()

	def start(self):
		self.server = DHTServerWorker()
		self.server.start()
