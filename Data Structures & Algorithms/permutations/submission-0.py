class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(current):
            if len(current) == len(nums):
                result.append(current.copy())
            for i in range(len(nums)):
                if nums[i] in current:
                    continue
                current.append(nums[i])
                backtrack(current)
                current.pop()
            
        backtrack([])
        return result
            
            
        