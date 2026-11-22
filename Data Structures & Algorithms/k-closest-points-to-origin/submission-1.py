import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        x2,y2 = 0,0
        result = []
        
        for x,y in points:
            distance = math.sqrt((x - x2)**2 + (y - y2)**2)
            heapq.heappush(heap, (distance, [x,y]))
            heapq.heapify(heap)
        while k>0:
            answer = heapq.heappop(heap)
            heapq.heapify(heap)
            result.append(answer[1])
            k-=1
            
        return result
            


        