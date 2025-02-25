class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
    
        
        l = set()
        for i in range(9):
            rset = set()
            cset = set()
            for j in range(9):
                # check columnls
                if board[j][i]>="1" and board[j][i]<="9":
                    if board[j][i] in cset:
        
                        return False
                    cset.add(board[j][i])
                #check rows
                if board[i][j]>="1" and board[i][j]<="9":
                    if board[i][j] in rset:
    
                        return False
                    rset.add(board[i][j])
                
        for i in range(0,9,3):
            for j in range(0,9,3):
                mset = set()
                count = 0

                if board[i][j]>="1" and board[i][j]<="9":
                    mset.add(board[i][j])
                    count+=1
                if board[i][j+1]>="1" and board[i][j+1]<="9":
                    mset.add(board[i][j+1])
                    count+=1
                if board[i][j+2]>="1" and board[i][j+2]<="9":
                    mset.add(board[i][j+2])
                    count+=1
                if board[i+1][j]>="1" and board[i+1][j]<="9":
                    mset.add(board[i+1][j])
                    count+=1
                if board[i+2][j]>="1" and board[i+2][j]<="9":
                    mset.add(board[i+2][j])
                    count+=1
                if board[i+1][j+1]>="1" and board[i+1][j+1]<="9":
                    mset.add(board[i+1][j+1])
                    count+=1
                if board[i+2][j+1]>="1" and board[i+2][j+1]<="9":
                    mset.add(board[i+2][j+1])
                    count+=1
                if board[i+1][j+2]>="1" and board[i+1][j+2]<="9":
                    mset.add(board[i+1][j+2])
                    count+=1
                if board[i+2][j+2]>="1" and board[i+2][j+2]<="9":
                    mset.add(board[i+2][j+2])
                    count+=1

                if len(mset) != count:
                    return False

        return True






             


        