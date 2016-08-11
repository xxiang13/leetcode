# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 21:08:40 2016

@author: apple
"""

'''
Given two sorted integer arrays nums1 and nums2, merge nums2 
into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater 
or equal to m + n) to hold additional elements from nums2. 
The number of elements initialized in nums1 and nums2 are m and n respectively.
'''

##### save to a new array solution

# input: array1,length m,array2,length n

# output: none, do inplace sort, assme array1 can contians m+n elements

'''
pseudo code:

i=0
j=0
k=0

combined =[]

while i<array1 or j<array2:
    
    if array1[i]<array2[j]:
        combined.append(array[i])
        i+=1
    
    else:
        combined.append(array[i])
        j+=1
    
    k+=1
    

while i<array1:
    combined.append(array1[k])
    i+=1
    k+=1
    
while j<array2:
    combined.append(array2[k])
    j+=1
    k+=1
'''

##### inplace solution

# keep track of 3 pointers:
# i from m-1, j from n-1, and k from m+n-1
# start from the last element element (m-1, n-1, m+n-1)
# assume nums 1 has elements up to m-1 index, then remaning n elements (up to m+n-1 is empty)

# compare element from nums1 and nums2, assign biggest to end of array nums1, move index from array with biggest element
# keep repeating until run out of elements from either nums1 or nums2

# if there are remaning elements in nums2, then keep assigning to nums1

def merge(self, A, m, B, n):
    last, i, j = m + n - 1, m - 1, n - 1
    
    while i >= 0 and j >= 0:
        if A[i] > B[j]:
            A[last] = A[i]
            last, i = last - 1, i - 1
        else:
            A[last] = B[j]
            last, j = last - 1, j - 1
    
    while j >= 0:
            A[last] = B[j]
            last, j = last - 1, j - 1