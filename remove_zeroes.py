# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 21:31:50 2015

@author: Shawn Li

IDE: Spyder python 3.4
"""

'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.

'''

#%% Method 1: Time efficiency approximate: O (2N) since remove searches for 0 from beginning of list each time
def moveZeroes1(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """

    #indicesZeroes = [i for i,v in enumerate(nums) if v == 0]
    numZero = nums.count(0)
    
    for i in range(numZero):
        nums.remove(0) 
    
    nums.extend([0]*numZero)
    
    return nums

#%% Method 2 improves time efficiency to N
def moveZeroes2(nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zeroList = []
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                del nums[i]
                zeroList.append(0)
            else:
                i += 1
        
        nums.extend(zeroList)
        
        return nums
        
#%%Test
nums = [0, 1, 0, 3, 12]
moveZeroes1(nums)
moveZeroes2(nums)