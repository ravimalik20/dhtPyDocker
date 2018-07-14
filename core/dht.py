import hashlib
from storage.core import StorageEngine

class DHTNode:
	def __init__(self, name):
		self.name = name
		self.id = self.__hash(name)

		self.pred_port, self.succ_port = 0, 0

		self.storage = StorageEngine()

	def get(self, key):
		if self.__isOwner(key):
			return self.storage.get(key)

	def put(self, key, value):
		if self.__isOwner(key):
			return self.storage.put(key, value)

	def __hash(self, key):
		key = key.encode("utf-8")
		return hashlib.sha256(key).hexdigest()

	def __isOwner(self, key):
		return True

	def __str__(self):
		val = "Name:{}\nID:{}".format(self.name, self.id)
		return val
