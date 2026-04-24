class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        current_price = 0

        for price in prices:
            if min_price > price:
                min_price = price
            else:
                current_price = price - min_price
                max_profit = max(current_price, max_profit)
        return max_profit

        