from core import StorageEngine

class StorageEngineTest:
	def __init__(self):
		self.storage = StorageEngine()

	def run(self):
		print ("#### Testing Begin ####")

		for i in range(10):
			self.storage.put(i, 10*i)

		for i in range(10):
			val = self.storage.get(i)
			print("{}:{}".format(i, val))

		for i in range(5, 9):
			self.storage.put(i, i*100)

		for i in range(10):
			val = self.storage.get(i)
			print("{}:{}".format(i, val))

		print ("#### Testing End ####")

if __name__ == "__main__":
	t = StorageEngineTest()
	t.run()
