class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        r = list(str(x))
        if x<0:
            r = r[1:]
            t = int(''.join(r[::-1]))
            if t >2147483647:
                return 0
            return t*(-1)

        t = int(''.join(r[::-1]))
        if t >2147483647:
            return 0
        return t