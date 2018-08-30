import numpy as np
import matplotlib.pyplot as plt
import unittest

class Issue6921TestCase(unittest.TestCase):
	
	def test_numpoints_point_five(self):
		with self.assertRaises(ValueError) as context:
			lineup, = plt.plot([1,2,3], label='Line 2')
			linedown, = plt.plot([3,2,1], label='Line 1')
			plt.legend(numpoints = .5)
		self.assertTrue("'numpoints must be a whole number and greater than or equal to 1; it was', 0.5" in str(context.exception))

	def test_numpoints_one_point_zero(self):
		try:
			lineup, = plt.plot([1,2,3], label='Line 2')
			linedown, = plt.plot([3,2,1], label='Line 1')
			plt.legend(numpoints = 1.0)
		except ExceptionType:
			self.fail("numpoints = 1.0 raise Exception unexpectedly!")

	def test_numpoints_one_point_five(self):
		with self.assertRaises(ValueError) as context:
			lineup, = plt.plot([1,2,3], label='Line 2')
			linedown, = plt.plot([3,2,1], label='Line 1')
			plt.legend(numpoints = 1.5)
		self.assertTrue("'numpoints must be a whole number and greater than or equal to 1; it was', 1.5" in str(context.exception))

if __name__ == '__main__':
	unittest.main()