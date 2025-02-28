class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        aDict = {'I': 1, 'V': 5, 'X': 10, 'L':50, 'C': 100, 'D':500,'M': 1000, 'IV':4, 'IX':9, 'XL': 50, 'XC': 90, 'CD': 400, 'CM': 900}
        L = list(s)
           
        for i in range(len(L)-1): 
            if aDict.get(L[i])>=aDict.get(L[i+1]):
                sum+=aDict.get(L[i])     
            else:
                sum-=aDict.get(L[i])

        
        sum+=aDict.get(L[-1])
        return sum  
