# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


# Slow O(n2)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        delta = 0

        if len(prices) <= 1:
            return 0

        for idx, price_buy in enumerate(prices[:-1]):
            for price_sell in prices[idx:]:
                if price_sell - price_buy > delta:
                    delta = price_sell - price_buy

        return delta


# faster O(n)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) <= 1:
            return 0

        buy_price = prices[0]
        sell_price = prices[1]

        profit = max([0, sell_price - buy_price])

        for idx, price in enumerate(prices):

            if price < buy_price and idx < len(prices) - 1:
                buy_price = price
                sell_price = prices[idx + 1]
                profit = max([profit, sell_price - buy_price])

            if price > sell_price:
                sell_price = price
                profit = max([profit, sell_price - buy_price])

        return profit
