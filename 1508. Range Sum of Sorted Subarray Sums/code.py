class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        alist = list()
        anolist = list()
        for i in range(len(nums)):
            temp = 0
            for j in range(i, len(nums)):
                temp+= nums[j]
                alist.append(temp)
        alist.sort()
        return sum(alist[left-1:right])%(10**9 +7)

        