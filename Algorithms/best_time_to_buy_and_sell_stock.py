# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31

@author: Xiang Li
"""

'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.
'''

'''
Method 1: try every buy & sell days combinaton
since sell days can't be earlier than buy days
the all possibile combinations = n+(n-1)+(n-2)+...+1 = n(n+1)/2
each iteration is constant time, so time complexity here O(n^2)
'''

'''
Method 2: let one pointer iterate the list, update lower price to be buy price,
and compare profit with current max profit, save max profit from each iteration
- Always save max profit so far and compare with next one (Dynamic programming)
Time complexity O(n) since iterate the whole list
'''
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        # edge case, empty/1 element list
        if len(prices) <= 1:
            return 0
            
        lowest_price = prices[0]
        max_profit = 0
        sell_day = None
        buy_day = None
        lowest_price_day = None
        
        for i in range(0,len(prices)):
            if prices[i] < lowest_price:
                # update lowest price
                lowest_price = prices[i]
                lowest_price_day = i # save current lowest price day
            
            gain= prices[i]-lowest_price
            max_profit = max(max_profit,gain) # update current max profit
            
            if max_profit == gain:
            # if max profit updated, save new buy/sell day
                buy_day = lowest_price_day
                sell_day = i
                
        print("buy_day: " + str(buy_day))
        print("sell_day: " + str(sell_day))
        
        return max_profit

#%% test
test = Solution()
prices = [7, 1, 5, 3, 6, 4]
test.maxProfit(prices)
    
        