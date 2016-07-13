# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12

@author: xiang li
"""

'''
You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, the only constraint 
stopping you from robbing each of them is that adjacent houses have security 
system connected and it will automatically contact the police if two adjacent
houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each
house, determine the maximum amount of money you can rob tonight without
alerting the police.


Solution (cited from linshiu)
Time: O(n)
Space: O(n)
Dynamic programming solution by saving subproblem solutions
A[i] = money in ith house
B[i] = max money for i houses
B[0] = 0
B[1] = A[i]
for house i, there are 2 cases:
1) Don't rob i th house, and rob best combination for the first i-1 houses
2) Rob ith house, and rob best combination for the first i-2  houses 
   (since house i-1 th cannot be robbed since house is ith is robbed and cannot be consecutive)
B[i] = max(0 + B[i-1], A[i]+B[i-2])

'''

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_houses = len(nums)
        values = [0]*(num_houses+1)
            
        if nums:
            values[1] = nums[0]
        
        for i in range(2,num_houses+1):
            values[i] = max(values[i-2]+nums[i-1],values[i-1])
        
        return values[num_houses]

#%% test
test = Solution()
test.rob([1,2,3,4,5])
test.rob([1,2])
test.rob([2,1])