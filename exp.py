# takes an integer x and non-neg integer y and returns x**y successive multiplication iteratively

def exp(x,y):
	total = 1
	for num in range (0,y):
		total = total*x
	return total

'''
Test Case:
>>> exp(2,0)
1
>>> exp(2,2)
4
>>> exp(2,3)
8
>>> exp(2,4)
16
'''
