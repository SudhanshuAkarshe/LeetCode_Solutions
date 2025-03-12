class Solution(object):
    def lengthOfLastWord(self, s):
        import re
        """

        :type s: str
        :rtype: int
        """
        
        l = s.split(' ')
        l = l[::-1]
        for i in l:
            if re.search('[a-zA-Z]',i) :
                return len(i)