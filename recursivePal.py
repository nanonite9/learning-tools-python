# Implement isPalindrome recursively.
# The base case is that s is a palindrome if it has 0 or 1 characters. The inductive case is that 
# s is a palindrome if its first and last character are the same and the 'middle' part without 
# the first and last character is a palindrome.

def recursivePal(s):
    if len(s) == 0:                               # part of the base case that s is a palindrome 
        return True                               # if it contains '0' characters
    if len(s) == 1:                               # part of the base case that s is a palindrome 
        return True                               # if it contains '1' character
    if s[0] == s[-1] and isPalindrome(s[1:-1]):   # showing the inductive case
        return True
    else:
        return False
