class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(index, current):
            if sorted(current) not in result:
                result.append(sorted(current.copy()))
            for i in range(index, len(nums)):
                current.append(nums[i])
                backtrack(i+1, current)
                current.pop()
        
        backtrack(0, [])
        return result
        