class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        tracker = []
        def backtrack(index, current):
            if sum(current) == target:
                tracker.append(current.copy())
            for i in range(index, len(nums)):
                current.append(nums[i])
                if sum(current) <= target:
                    backtrack(i, current)
                current.pop()

        backtrack(0, [])
        return tracker 
        