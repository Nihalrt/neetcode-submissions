class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        num_set = set(nums)

        for x in num_set:
            if (x-1) not in num_set:
                curr = x
                curr_len = 1

                while (curr+1) in num_set:
                    curr = curr+1
                    curr_len+=1
                
                max_len = max(max_len, curr_len)
        return max_len



        