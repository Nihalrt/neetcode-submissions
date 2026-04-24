class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_list = [1] * n
        suffix_list = [1] * n
        prefix = 1
        suffix = 1
        for i in range(n):
            prefix_list[i] = prefix
            prefix*=nums[i]
            j = n-1-i
            suffix_list[j] = suffix
            suffix*=nums[j]
        result = [prefix_list[i]*suffix_list[i] for i in range(n)]
        return result

        