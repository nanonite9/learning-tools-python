# a function that returns a pair with the two solutions in the 
# quadratic equation, assume coefficients are floating point numbers
# a function that supports complex numbers

from math import sqrt                 

def quadraticEquation(a, b, c):         #quadratic formula
    x1 = ((-b)+(sqrt((b**2)-(4*a*c))))/(2*a)
    x2 = ((-b)-(sqrt((b**2)-4*a*c)))/(2*a)
    return (x1, x2)

from cmath import sqrt                          

def quadraticEquationComplex(a, b, c):  #quadratic formula with complex solutions
    x1 = ((-b)+(sqrt((b**2)-(4*a*c))))/(2*a)
    x2 = ((-b)-(sqrt((b**2)-4*a*c)))/(2*a)
    return (x1, x2)

'''
Test Case:
>>> quadraticEquationComplex(1, 10, 34)
((-5+3j), (-5-3j))
'''
