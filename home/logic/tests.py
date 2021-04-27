import unittest
from mainLogic import extract_ids, extract_transactions, apdata_prepare
import pandas as pd

class Test(unittest.TestCase):
	def testing_funtion_extract_ids(self):
		age = [10,20,30,40,50,45,47,50,49]
		id = [1,2,3,4,5,6,7,8,9]
		age_min = 40
		age_max = 50
		expected_output = set({4,5,6,7,8,9})
		self.assertSetEqual(expected_output, extract_ids(age, id, age_min, age_max))

		age = [10,20,30,40,50,45,47,50,49]
		id = [1,2,3,4,5,6,7,8,9]
		age_min = 60
		age_max = 65
		expected_output = set()
		self.assertSetEqual(expected_output, extract_ids(age, id, age_min, age_max))

		age = [10,20,30,40,50,45,47,50,49]
		id = [1,2,3,4,5,6,7,8,9]
		age_min = 40
		age_max = 30
		expected_output = set()
		self.assertSetEqual(expected_output, extract_ids(age, id, age_min, age_max))

	def testing_extract_transactions(self):
		df = pd.DataFrame([[1,'a','b','c'],[2,'b','c','d'],[1,'e','f'],[3,'b','d'],[4,'g','h','i'],[1,'x','q'],[5,'r']])
		s = set({1})
		expected_output = [['a','b','c'],['e','f'],['x','q']]
		self.assertCountEqual(expected_output, extract_transactions(df, s))
		s = set({1,3})
		expected_output = [['a','b','c'],['e','f'],['x','q'],['b','d']]
		self.assertCountEqual(expected_output, extract_transactions(df, s))
		s = set({6})
		expected_output = []	
		self.assertCountEqual(expected_output, extract_transactions(df, s))
		df = pd.DataFrame([[1,'a','b',],[2,'b','c','d'],[1,'e','f'],[3,'b','d'],[4,'g','h','i'],[1,'x','q'],[5,'r']])
		s = set({1})
		expected_output = [['a','b'],['e','f'],['x','q']]
		self.assertCountEqual(expected_output, extract_transactions(df, s))
		df = pd.DataFrame([[1,'a',None,'c'],[2,'b','c','d'],[1,'e','f'],[3,'b','d'],[4,'g','h','i'],[1,'x','q'],[5,'r']])
		s = set({1})
		expected_output = [['a','c'],['e','f'],['x','q']]
		self.assertCountEqual(expected_output, extract_transactions(df, s))
		df = pd.DataFrame([[1,None ,None,'c'],[2,'b','c','d'],[1,'e','f'],[3,'b','d'],[4,'g','h','i'],[1,'x','q'],[5,'r']])
		s = set({1})
		expected_output = [['c'],['e','f'],['x','q']]
		self.assertCountEqual(expected_output, extract_transactions(df, s))
		df = pd.DataFrame([[1,None ,None,None],[2,'b','c','d'],[1,'e','f'],[3,'b','d'],[4,'g','h','i'],[1,'x','q'],[5,'r']])
		s = set({1})
		expected_output = [[],['e','f'],['x','q']]
		self.assertCountEqual(expected_output, extract_transactions(df, s))

	def testing_function_apdata_prepare(self):
		labels = [0,0,1,2,1]
		ids = [1,2,3,4,5]
		expected_output = {0:[['a','b','c'],['b','c','d'],['e','f'],['x','q']], 1 : [['b','d'],['r']], 2:[['g','h','i']]}
		self.assertDictEqual(expected_output, apdata_prepare('test_file.csv', labels, ids))
		
	# def testing_function_giveOnlyProds(self):
	# 	df = pd.DataFrame([[1,'a','b','c'],[2,'b','c','d'],[3,'c','a','b'],[4,'d','g','b']])
	# 	expected_output = {'a':3, 'b':4,'c':3,'d':1,'g':1}
	# 	self.assertDictEqual(expected_output, giveOnlyProds(df))


if __name__ == "__main__":
    unittest.main()