from typing import Dict,List

def gen_delta(start,end,delta):
	'''
	generate a set of tuples from x to y using a delta of z
  
  example: input (1,20,10)
  return: 
  (1, 10)
  (11, 20)
	'''
	curr = start
	while curr < end:
		yield curr, min(curr+delta-1,end)
		curr += delta	

def gen_pair(input_list:list) -> dict:
	'''
	uses `typing`
	given a list [1,2,3,4]
	splits list into every OTHER element into two other lists
	then creates a dict of the result values

	'''
	field_left = input_list[::2]
	field_right = input_list[1::2]
	return dict(zip(field_left,field_right))

print(gen_pair([1,'2',3,4]))