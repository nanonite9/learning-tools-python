# Check if a word is a palindrome

def rev(s):
    return s if s == "" else rev(s[1:]) + s[0]

def recPalindrome(s):
    s.isalpha()
    s.lower()
    if rev(s) == s:
        return True
    else:
        return False


def rev(s):
return s if s =="" else rev(s[1:]) + s[0]
