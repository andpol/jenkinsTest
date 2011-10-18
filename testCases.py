import mylib
import unittest

class TestSequence(unittest.TestCase):
	def setUp(self):
	#Gets called before EACH test
		pass
	def tearDown(self):
	#Gets called after EACH test
		pass

	#The Tests:
	def test_add_simple(self):
		self.assertEqual(mylib.add(1,1), 2)

	def test_add_negatives(self):
		self.assertEqual(mylib.add(-1,3), 2)

if __name__=="__main__":
	unittest.main()
