class Solution:
    def mySqrt(self, x: int) -> int:
        l,h = 0, x
        res = 0
        if x == 0:
            return res

        while l<=h:
            mid = (l+h)//2
            if mid*mid<=x:
                res = mid
                l = mid+1
            else:
                h = mid-1

        return res