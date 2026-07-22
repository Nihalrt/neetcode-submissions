class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        store = {
            2:"abc",
            3:"def",
            4:"ghi",
            5:"jkl",
            6:"mno",
            7:"pqrs",
            8:"tuv",
            9:"wxyz"
        }
        if not digits:
            return []
        result = []
        def backtrack(index, current):
            if len(current)==len(digits):
                result.append(current)
                current = ""
                return
            current_digit = digits[index]
            letters = store[int(current_digit)]
            for i in letters:
                backtrack(index+1, current+i)
        backtrack(0,"")
        return result
                    
        