import unittest
import sample

class TestSampleFunc(unittest.TestCase):
	def setUp(self):
		pass

	def test_sample_func(self):
		result = sample.sample_func(1)
		self.assertEqual(result,"One")

	def test_sample_func2(self):
		result = sample.sample.sample_func(2)
		self.assertEqual(result,"Something else")

if __name__ == '__main__':
	unittest.main()