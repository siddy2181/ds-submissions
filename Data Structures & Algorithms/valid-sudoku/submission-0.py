class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet = defaultdict(set)
        colSet = defaultdict(set)
        subboxSet = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if(board[r][c] in rowSet[r]):
                    return False
                if(board[r][c] in colSet[c]):
                    return False
                if(board[r][c] in subboxSet[(r//3,c//3)]):
                    return False
                
                rowSet[r].add(board[r][c])
                colSet[c].add(board[r][c])
                subboxSet[(r//3,c//3)].add(board[r][c])

        
        return True

