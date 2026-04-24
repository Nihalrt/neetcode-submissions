class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Hashmap = {}
        k = ""
        for x in strs:
            k = "".join(sorted(x))
            if k not in Hashmap:
                Hashmap[k] = []
            Hashmap[k].append(x)
        return list(Hashmap.values())
     


        