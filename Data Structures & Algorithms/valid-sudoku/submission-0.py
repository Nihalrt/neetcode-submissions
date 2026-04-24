class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxes = [set() for _ in range(9)]
        for x in range(9):
            row = set()
            column = set()
            for y in range(9):
                if board[x][y] != ".":
                    if board[x][y] in row:
                        return False
                    row.add(board[x][y])
                if board[y][x] != ".":
                    if board[y][x] in column:
                        return False
                    column.add(board[y][x])
                
                if board[x][y]!=".":
                    box_i = (x//3) * 3 + (y//3)
                    if board[x][y] in boxes[box_i]:
                        return False
                    boxes[box_i].add(board[x][y])
        return True
        


            


                

             


        