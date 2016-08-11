# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 

@author: Xiang Li
"""

'''
Given a sorted array, remove the duplicates in place such that each element 
appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place 
with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums 
being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.
'''

'''
solution
set two ponters: one static: last; one dynamic: i
compare nums[last] =? nums[i]
if yes move i to right; if not, change nums[last+1] = nums[i] and last=last+1
by doing this, it always assign different value than num[last] to the next
value: nums[last+1], until i iterage whole array, so first (last+1) numbers
element without duplicates since array staring from 0

Time complexity: O(n) since iterate whole array
Space complexity: O(1) in-place assigning values
'''

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # edge case: if array is empty
        if not nums:
            return 0
            
        last,i = 0,1
        
        while i < len(nums):
            if nums[last] != nums[i]:
                last = last + 1
                nums[last] = nums[i]
            i += 1
        
        return last+1
                