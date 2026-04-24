class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        temp_stack = []

        for curr_i, curr_temp in enumerate(temperatures):
            while temp_stack and curr_temp > temperatures[temp_stack[-1]]:
                past_i = temp_stack.pop()
                result[past_i] = curr_i - past_i
            temp_stack.append(curr_i)
        return result
            


    

        