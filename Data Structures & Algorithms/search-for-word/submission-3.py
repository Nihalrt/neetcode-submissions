class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLMS = len(board), len(board[0])
        path = set()
        def backtrack(row, col, word_index):
            if word_index==len(word):
                return True
            
            if (row < 0 or col < 0 or 
                row >= ROWS or col >= COLMS or 
                board[row][col] != word[word_index] or 
                (row, col) in path):
                return False
            
            
            path.add((row, col))
            found = (backtrack(row-1, col, word_index+1) or
            backtrack(row+1, col, word_index+1) or
            backtrack(row, col+1, word_index+1) or
            backtrack(row, col-1, word_index+1))
            path.remove((row,col))
            return found

        for r in range(ROWS):
            for c in range(COLMS):
                if backtrack(r, c, 0):
                    return True
        return False
            
                


            

                

        