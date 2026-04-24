class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Hash = {}
        buckets = [[] for _ in range(len(nums)+1)]
        result = []
        for x in nums:
            if x not in Hash:
                Hash[x] = 1
            else:
                Hash[x]+=1

        for y in Hash:
            buckets[Hash[y]].append(y)
        for i in range(len(buckets)-1, -1, -1):
            if buckets[i]!=[]:
                result+=buckets[i]
            if len(result)>=k:
                return result

            
            


        
        