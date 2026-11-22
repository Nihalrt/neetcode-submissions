import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums)==1:
            return nums[0]
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        return nums[0]
        
        