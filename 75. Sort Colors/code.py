class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        #doesnt work as one pass algorithm
        zero = nums.count(0)
        one = nums.count(1)
        two = nums.count(2)

        for i in range(zero):
            nums[i] = 0
        for i in range(zero,zero+one):
            nums[i] = 1
        for i in range(zero+one, len(nums)):
            nums[i] = 2
        