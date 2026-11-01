class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # res = False
        # def checkDuplicate(arr):
        #     tempSet = set()
        #     for i in arr:
        #         if i in tempSet:
        #             return False
        #         else:
        #             if i != '.':
        #                 tempSet.add(i)
        #     return True


        # for rows in board:
        #     res = checkDuplicate(rows)
        
        rowSet = defaultdict(set)
        colSet = defaultdict(set)
        subBoard = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if board[r][c] in rowSet[r]:
                    return False
                if board[r][c] in colSet[c]:
                    return False
                if board[r][c] in subBoard[(r//3,c//3)]:
                    return False
                rowSet[r].add(board[r][c])
                colSet[c].add(board[r][c])
                subBoard[(r//3,c//3)].add(board[r][c])
        return True



