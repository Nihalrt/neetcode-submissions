class Solution:
    def isValid(self, s: str) -> bool:
        result = []
        if s[0]==')' or s[0]==']' or s[0]=='}':
            return False
        for bracket in s:
            if result and ((result[-1]=='(' and bracket==')') or (result[-1]=='[' and bracket==']') or (result[-1]=='{' and bracket=='}')):
                result.pop()
            else:
                result.append(bracket)
        return len(result)==0
        