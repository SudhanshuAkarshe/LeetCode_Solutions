class Solution:
    def hIndex(self, citations: List[int]) -> int:
        max = -1
        """size =-1
        for h in citations:
            l = len(citations)-citations.index(h)+1
            if h>max and h<=l :
                max = h
                size = l
        return max"""

    

        low,high = 0, len(citations)-1

        while low<=high:
            mid = (low+high)//2
            if citations[mid]>= len(citations)-mid:
                high = mid -1
            else:
                low = mid +1
        return len(citations)-low


        