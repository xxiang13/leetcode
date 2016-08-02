# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31

@author: Xiang Li
"""

'''
Given an integer array nums, find the sum of the elements between indices i and
 j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function. **** could call n times
'''

'''
method 1: iterate from starting to the end, each time add up values
worse case iterate whole list for each case, if call n cases
time complexity O(n^2)
'''

'''
method 2: store all aggregate sum for each index sum(i)
** sum(i+1) = sum(i) + value[i+1]
** sum of range i,j = sum(j+1) - sum(i)
'''
class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        if not nums:
            self.sums = None
        else:
            size = len(nums)
            self.sums = [0]*(size+1)

            for i in range(size):
                self.sums[i+1] = self.sums[i] + nums[i] 
                # each sum exclude value of index i
        
        

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if not self.sums:
            return None
        # since sum exclude value of index i, j+1 get sum of first j index
        return self.sums[j+1] - self.sums[i] 
                 
#%% test
# Your NumArray object will be instantiated and called as such:
numArray = NumArray([-2, 0, 3, -5, 2, -1])
numArray.sumRange(0, 1)
numArray.sumRange(1, 2)