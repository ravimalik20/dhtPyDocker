from dht import DHTNode

class NodeTest:
	def __init__(self):
		pass

	def run(self):
		n1 = DHTNode("node1")
		print (n1)

		for i in range(15):
			n1.put(i, i+10)
			print ("{}".format(n1.get(i)))

if __name__ == "__main__":
	t = NodeTest()
	t.run()
