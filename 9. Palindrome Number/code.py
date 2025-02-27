class Solution(object):
    def isPalindrome(self, x):
        l = list(str(x))
        reverse = ''.join(l[::-1]) 
        if str(x) == reverse:
            return True
        return False
