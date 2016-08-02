# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 21:53:38 2016

@author: apple
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

1st pointer move if its value less than 2nd pointers
if meet same value, both ponters move to right by 1 until finishing iterating
smaller array

Worse case time complexity O(m+n) since linearly iterate both arrays
Space complexity O(1)

'''