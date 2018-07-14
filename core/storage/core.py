class StorageEngine:
	def __init__(self):
		self.storage = dict()

	def __len__(self):
		return len(self.storage)

	def get(self, key):
		if key not in self.storage:
			return None

		return self.storage[key]

	def put(self, key, value):
		self.storage[key] = value
