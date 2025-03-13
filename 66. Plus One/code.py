class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s = 0
        for i in range(len(digits)):
            s = s + digits[i] * (10**((len(digits)-1-i)))
        

        s+=1
        l = list(map(int,str(s)))
        return l

        