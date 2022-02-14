class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows,cols=len(board),len(board[0])
        
        row_d=set()
        col_d=set()
        inner_d=set()
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j]!='.':
                    
                    if (i,board[i][j]) not in row_d and (j,board[i][j]) not in col_d and ((i//3,j//3),board[i][j]) not in inner_d:
                        row_d.add((i,board[i][j]))
                        col_d.add((j,board[i][j]))
                        inner_d.add(((i//3,j//3),board[i][j]))
                    else:
                        return False
        
        return True
