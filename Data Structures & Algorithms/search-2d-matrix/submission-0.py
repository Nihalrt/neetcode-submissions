class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)-1

        while l<=r:
            mid_row = (l+r) // 2
            if target > matrix[mid_row][-1]:
                l = mid_row + 1
            elif target < matrix[mid_row][0]:
                r = mid_row - 1
            else:
                break
        
        if not l<=r:
            return False
        
        row = (l+r) // 2
        x,y = 0, len(matrix[0]) - 1

        while x<=y:
            m = (x+y) // 2
            if target > matrix[row][m]:
                x = m+1
            elif target < matrix[row][m]:
                y = m-1
            else:
                return True
        return False

        
        