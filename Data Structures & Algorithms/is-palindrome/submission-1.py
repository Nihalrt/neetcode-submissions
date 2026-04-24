class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = "".join(filter(str.isalnum, s))
        final = string[::-1]
        return final.lower()==string.lower()

        