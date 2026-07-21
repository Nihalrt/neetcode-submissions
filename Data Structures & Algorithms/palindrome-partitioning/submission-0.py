class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        def backtrack(start, current):
            if start == len(s):
                result.append(current.copy())
                return
            
            for i in range(start, len(s)):
                if s[start:i+1] == s[start:i+1][::-1]:
                    current.append(s[start:i+1])
                    backtrack(i+1, current)
                    current.pop()
        backtrack(0,[])
        return result
        