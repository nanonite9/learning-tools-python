# use isPalindromePlus(s) to check whole sentences while ignoring capitalization, space, and punctuation.

# check result with this function to compare
def isPalindrome(s):
	for i in range (len(s)//2):
		if s[i] != s[-i-1]:
			return False
		else:
			return True                     #palindrome function given in lecture

# converts uppercase to lowercase letters and removes everything that is not a letter		
def onlyLetters(s):
	s = s.lower()                                   #makes it all lowercase
	s = s.replace(" ","")                           #removes spaces
	s = "".join([c for c in s if c.isalpha()])      #only takes letters
	return s

def isPalindromePlus(s):
	w = onlyLetters(s)                              #checks whole sentence while ignoring caps, space, and punctuation
	return isPalindrome(w)
'''
Test Case:
>>> onlyLetters('Was it a car or a cat I saw?')
'wasitacaroracatisaw'
>>> isPalindromePlus('Was it a car or a cat I saw?')
True
'''
