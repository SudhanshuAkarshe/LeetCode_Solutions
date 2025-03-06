class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        temp = list(set(nums))
        temp.sort()
        leg = len(temp)
            
        for i in range(leg):
            nums[i] = temp[i]    
        return leg