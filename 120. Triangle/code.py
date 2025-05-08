class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        #Starting from bottom-1 layer(i) to top
        #check minimum sum(j) of left and right element right below(i)
        
        for i in range(len(triangle)-2,-1,-1):
            for j in range(len(triangle[i])):
                triangle[i][j]+= min(triangle[i+1][j], triangle[i+1][j+1])

        return triangle[0][0]