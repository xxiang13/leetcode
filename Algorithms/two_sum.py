# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4

@author: Xiang Li
"""

'''
Given an array of integers, return indices of the two numbers such that they 
add up to a specific target.

You may assume that each input would have exactly one solution.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
UPDATE (2016/2/13):
The return format had been changed to zero-based indices. Please read the 
above updated description carefully.
'''

#Clarify: is the array ordered?


# Assume not sorted:

'''
Method 1: sort array + binary search
First sort array (e.g. quicksort/merge sort = O(nlog(n)) otherise exponential
since need to check every possible combination

After sorted
iterate for all numbers < target/2 since a value has only one possible way to add up
to the target (e.g iterate numbers < 5 if target 9 )

for each number, then do a binary search for the number target - number (e.g. 8) in
the section of the array between target/2 (eg. 5) and target (9) to find if target -number
is in the array    
* Time complexity O(log(n)*n)
* Space complexity O(1)
'''

'''  
Method 2: hash table
keep a lookup : key = number, value = index
iterate index,num in array
if (target - num) in lookup --> return indies
if not add {num:index} to lookup

since hash table check by value is constant time
* time complexity O(n)
* space complexity O(n)
'''

def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    lookup = {}
    for i, num in enumerate(nums):
        if target - num in lookup:
            return [lookup[target - num], i]
        lookup[num] = i
    return []