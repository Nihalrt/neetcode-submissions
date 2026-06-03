from collections import Counter, defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = defaultdict(int)
        s1_dict = Counter(s1)
        k = len(s1)

        for right in range(len(s2)):
            window[s2[right]] += 1
            if (right+1) == k:
                if window == s1_dict:
                    return True
            
            elif (right+1) > k:
                window[s2[right-k]]-=1
                if window[s2[right-k]]==0:
                    del window[s2[right-k]]
                
                if window==s1_dict:
                    return True
        return False


        
        
        