import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        mid = 0
        res = right

        while left<=right:
            mid = (left + right)//2

            total_hrs = 0
            for p in piles:
                total_hrs+=math.ceil(p/mid)
            
            if total_hrs<=h:
                res = mid
                right = mid - 1
            if total_hrs > h:
                left = mid + 1
        return res



        