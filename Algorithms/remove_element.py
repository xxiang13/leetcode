# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4

@author: Xiang Li
"""

'''
Given an array and a value, remove all instances of that value in place 
and return the new length.

Do not allocate extra space for another array, you must do this in place 
with constant memory.

The order of elements can be changed. It doesn't matter what you leave 
beyond the new length.

Example:
Given input array nums = [3,2,2,3], val = 3

Your function should return length = 2, with the first two elements of 
nums being 2.
'''

'''
Solution: move all instances = target to the end of array
set two pointer: left, right iterating from both side of the array
left += 1 if nums[left] != target;
right -= 1 if nums[right] == target
since order doesn't matter, when nums[left] == target and nums[left] != target,
swap the two value and left += 1, right += 1 until left>= right
so nums[:left+1] are the desired result

Time complexity: O(n) worse case iterate whole array
Space complexity: O(1) in-place swapping
'''

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0
            
        left,right = 0,len(nums)-1
        
        while left <= right:
            if nums[left] != val:
                left += 1
            if nums[right] == val:
                right -= 1
            if nums[left] == val and nums[right] != val:
                nums[left],nums[right] = nums[right],nums[left]
                left += 1
                right -= 1
                
        return right+1