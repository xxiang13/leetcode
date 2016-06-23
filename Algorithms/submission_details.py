# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22

@author: Xiang Li
"""

'''
Given an array of size n, find the majority element. 
The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the 
majority element always exist in the array.

'''

'''
save counts to dictionary
until hit a case a count > n/2
worse case: freq > n/2 happens at last element in the list
so need to check each element, O(n)
'''
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        freq = {}
        
        for i in nums:
            freq[i] = freq.get(i,0) + 1    
            if freq[i] > len(nums)/2:
                    return i
#%% test
a = Solution()
a.majorityElement([1])