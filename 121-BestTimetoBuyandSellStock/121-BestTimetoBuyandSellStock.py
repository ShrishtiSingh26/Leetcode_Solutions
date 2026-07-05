# Last updated: 7/5/2026, 7:54:16 PM
1class Solution(object):
2    def maxProfit(self, prices):
3        min_price = float('inf')
4        max_profit = 0
5        
6        for price in prices:
7            if price < min_price:
8                min_price = price
9            else:
10                max_profit = max(max_profit, price - min_price)
11        
12        return max_profit