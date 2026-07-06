class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        tracker = []
        def backtrack(index, current_subset):
            tracker.append(current_subset.copy())
            for i in range(index, len(nums)):
                current_subset.append(nums[i])
                backtrack(i+1, current_subset)
                current_subset.pop()
        
        backtrack(0, [])
        return tracker

        