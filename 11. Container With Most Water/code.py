class Solution:
    def maxArea(self, height: List[int]) -> int:
       
        maax = 0
        l = 0
        r = len(height)-1
        while l<r:
            a = min(height[l], height[r]) * (r-l)
            maax = max(maax,a)

            if height[l]>height[r]:
                r-=1
            else:
                l+=1
        return maax

