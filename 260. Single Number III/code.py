class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
      #doesnt have linear space complexity
        s = set()
        for ele in nums:
            if ele in s:
                s.remove(ele)
            else:
                s.add(ele)

        return list(s)
            
            