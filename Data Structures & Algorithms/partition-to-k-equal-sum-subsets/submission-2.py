class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False
        target = sum(nums) // k
        used = [False]*len(nums)

        def backtrack(index, k, current_sum):
            if k==0:
                return True
            if current_sum==target:
                return backtrack(0, k-1, 0)
            for i in range(index, len(nums)):
                if used[i] or current_sum + nums[i] > target:
                    continue
                used[i] = True
                if backtrack(i+1,k,current_sum+nums[i]):
                    return True
                used[i] = False
            return False
        return backtrack(0,k,0)


            

        