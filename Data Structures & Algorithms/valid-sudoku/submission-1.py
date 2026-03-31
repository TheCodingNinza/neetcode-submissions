class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        s = set()
        for row in board:
            s.clear()
            for ch in row:
                if ch != ".":
                    if ch in s:
                        return False;
                    else:
                        s.add(ch)

        for x in range(9):
            s.clear()
            for y in range(9):
                if board[y][x] != ".":
                    if board[y][x] in s:
                        return False;
                    else:
                        s.add(board[y][x])
        box_mapper = [[0,0], [0,3], [0,6], [3,0], [3,3], [3,6], [6,0], [6,3] , [6,6]]                

        for i in range(9):
            s.clear()
            x = box_mapper[i][0]
            y = box_mapper[i][1]
            for m in range(x, x + 3, 1):
                for n in range(y, y + 3, 1):
                    if board[m][n] != ".":
                        if board[m][n] in s:
                            return False
                        else:
                            s.add(board[m][n])     
        return True            