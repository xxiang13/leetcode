# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1

@author: Xiang Li
"""

'''
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.

Follow up:
What if the given array is already sorted? How would you optimize your algorithm?

What if nums1's size is small compared to nums2's size? Which algorithm is better?

What if elements of nums2 are stored on disk, and the memory is limited such 
that you cannot load all elements into the memory at once?
'''

'''
######   Method 1: hash table (dictionary)  #######
save shorter array elements and its counts in a dictionary
iterate longer array, if elements in dictionrary, decrease one from its counts
and add the elements in the final result until counts < 0

since need to iterate longer array and unique elements in shoter array
worse case would be O(n^2)
'''

'''
## If the given array already sorted, and (m << n or m >> n)
Method 2: (sort) and binary search

since arrays are already sorted -> 
binary search here time complexity O(min(m, n) * log(max(m, n)))
Space complexity O(1) not saving any to memory
'''


'''
## If the given array already sorted, and (m << n or m >> n)
Method 3: (sort) and two pointers

one pointer iterate larger array, 2nd pointer iterage smaller array

1st pointer move to right if its value < 2nd pointers
2nd pointer move to right if its value < 1st pointers
if meet same value, both ponters move to right by 1 and save the value
until finishing iterating smaller array

Worse case time complexity O(m+n) since linearly iterate both arrays
Space complexity O(1)

'''

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort(), nums2.sort()  # Make sure it is sorted, doesn't count in time.

        intersection = []
        
        i1, i2 = 0, 0
        while i1 < len(nums1) and i2 < len(nums2):
        # iterate until smaller arrays finished
            if nums1[i1] < nums2[i2]:
                i1 += 1
            elif nums1[i1] > nums2[i2]:
                i2 += 1
            else:
                intersection += nums1[i1],
                i1 += 1
                i2 += 1
        
        return intersection