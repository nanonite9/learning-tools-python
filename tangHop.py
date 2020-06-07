# every time Miss Tang asks an easy question, she hops once. For every hard question, she hops twice.
# this function returns the total hops from Miss Tang.
def tangHop(easy, hard):
	return easy + 3*hard    # hops once for easy question, hops three times for hard question

'''
Test Case:
>>> tangHop(2,1)
5
'''
