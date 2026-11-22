import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        x, y = 0, 0

        while len(stones) > 1:
            x = heapq.heappop(stones)
            heapq.heapify_max(stones)
            y = heapq.heappop(stones)
            if x < y:
                y = y - x
                heapq.heappush(stones, y)
            if y < x:
                x = x - y
                heapq.heappush(stones, x)
            heapq.heapify_max(stones)
        return stones[0] if stones else 0






            
        