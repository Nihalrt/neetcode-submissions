class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks) % 4!=0:
            return False
        value = sum(matchsticks) / 4
        matchsticks.sort(reverse=True)
        used = [False] * len(matchsticks)

        def backtrack(sides_done, index, current_len):
            if sides_done == 3:
                return True
            if current_len == value:
                return backtrack(sides_done+1, 0, 0)

            for i in range(index, len(matchsticks)):
                if used[i] or current_len + matchsticks[i] > value:
                    continue
                used[i] = True
                if backtrack(sides_done, i+1,current_len + matchsticks[i]):
                    return True
                used[i] = False

            return False
        return backtrack(0,0,0)

        
