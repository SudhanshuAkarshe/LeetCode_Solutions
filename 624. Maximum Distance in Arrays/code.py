class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        small = arrays[0][0]
        big = arrays[0][-1]
        res = 0

        for i in range(1,len(arrays)):
            arr_min = arrays[i][0]
            arr_max = arrays[i][-1]

            res = max(res,abs(arr_min-big),abs(arr_max-small))

            small = min(arr_min,small)
            big = max(arr_max,big)
            
        return res

        