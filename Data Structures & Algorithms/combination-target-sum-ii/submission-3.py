class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        def backtrack(index, current):
            if sum(current) == target:
                result.append(current.copy())
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:

                    continue
                current.append(candidates[i])
                if sum(current) <= target:
                    backtrack(i+1, current)
                current.pop()
        backtrack(0, [])
        return result

        