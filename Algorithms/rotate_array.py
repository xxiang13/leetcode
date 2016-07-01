# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30

@author: Xiang Li
"""

'''
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7]
is rotated to [5,6,7,1,2,3,4].
Could you do it in-place with O(1) extra space?
'''

#%% method 1: pop last one and insert to beginning
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        shift = k% len(nums)
        
        if shift != 0:
            while shift >= 1:
                to_move = nums.pop()
                nums.insert(0,to_move)
                shift -= 1

#%% method 2: swap two chunks
class Solution2(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        shift = k% length
        if shift != 0:
            nums[0:k],nums[k:length] = nums[length-k:length], nums[0:length-k]
            
#%% test
test = Solution2()
a = [1,2,3,4,5]
test.rotate(a,2)
print(a)