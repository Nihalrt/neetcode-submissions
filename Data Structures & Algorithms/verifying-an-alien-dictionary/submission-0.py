class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {char: index for index, char in enumerate(order)}
        i = 0
        while i+1 < len(words):
            wordA = words[i]
            wordB = words[i+1]
            min_len = min(len(wordA), len(wordB))
            for j in range(min_len):
                if order_map[wordA[j]] > order_map[wordB[j]]:
                    return False
                elif order_map[wordA[j]] < order_map[wordB[j]]:
                    break
            else:
                if len(wordA) > len(wordB):
                    return False
            i+=1
        return True

        