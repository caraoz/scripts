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
