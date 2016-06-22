# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21

@author: Xiang Li
"""

'''
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

Note:
Each element in the result must be unique.
The result can be in any order.
'''

#%% 
'''
worse case: no duplicated value in both list, 
need to compare elements of one of the sets
time efficiency O(n)
'''
def intersection(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    set1 = set(nums1)
    set2 = set(nums2)
    intersect = []
    if len(set1) < len(set2):
        for i in set1:
            if i in set2:
                intersect.append(i)
    else:
        for i in set2:
            if i in set1:
                intersect.append(i)
    return intersect

    
#%% test
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
intersection(nums1, nums2)