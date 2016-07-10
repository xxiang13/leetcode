# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10

@author: Xiang Li
"""

'''
Given an array of integers and an integer k, find out whether 
there are two distinct indices i and j in the array such that nums[i] = nums[j] 
and the difference between i and j is at most k.
'''

'''
use feature of set() to compare if there dupdates in each K length
window. worse time complexity O(n)
'''

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(set(nums)) == len(nums):
            return False
        
        if k == 0:
            return False
            
        if len(nums) <= k:
            return len(set(nums)) < len(nums)
            
        begin = 0
        end = len(nums)-1-k
        
        while begin <= end:
            if len(set(nums[begin:begin+k+1])) <= k:
                return True
            
            else:
                begin += 1
                
        
        return False
                
#%% test
if __name__ == "__main__":
    test = Solution()
    
    nums = [4,2,5,0,3,4,3]
    k = 2
    
    print(test.containsNearbyDuplicate(nums,k))
    
    nums = [4,2,5,0,3,4,3]
    k = 1
    
    print(test.containsNearbyDuplicate(nums,k))
    
    nums = [1,2,1]
    k = 2
    
    print(test.containsNearbyDuplicate(nums,k))
    
    nums = [1,1]
    k = 1
    
    print(test.containsNearbyDuplicate(nums,k))
    
#%%
test2 = Solution()
test2.containsNearbyDuplicate([1,2,1],1)