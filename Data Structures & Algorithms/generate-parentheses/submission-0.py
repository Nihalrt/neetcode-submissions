class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def backtrack(current, open_count, close_count):
            if (len(current)==2*n) and (open_count==n and close_count==n):
                result.append(current)
                current = ""
            
            if open_count < n:
                backtrack(current + "(", open_count+1, close_count)
            
            if close_count < open_count:
                backtrack(current + ")", open_count, close_count+1)
        
        backtrack("", 0, 0)
        return result
            

        