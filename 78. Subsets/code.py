class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        final = [[]]

        for ele in nums: 
            final += [temp + [ele] for temp in final]
            
        return final
        