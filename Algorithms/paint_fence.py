# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31

@author: xiang li
"""

'''
There is a fence with n posts, each post can be painted with one of the k colors.

You have to paint all the posts such that no more than two adjacent fence posts 
have the same color.

Return the total number of ways you can paint the fence.

Note:
n and k are non-negative integers.
'''

'''
solution: first to clarify the question. 'posts such that no more than two 
adjacent fence posts' -> two adjacent fence can be same or different colors

dynamic programming: store total number of ways up to previous each fences,
considering result of current fence -> how many new ways would bring

assume total number up to current fences M(i)

current fence can have two result: same color as previous fence or different

same color - means previous fence has different color with the one before it
precious fence can choose k-1 colors, current fence since same color with
previous one, can think they as a same fence, so for them can choose k-1. 
--> M(i) = (k-1)* M(i-2)

different color - current fence can choose k-1 colors. M(i) = (k-1)* M(i-1)

total ways up to ith fence = sum of both cases =  (k-1)* (M(i-1) + M(i-2))
'''

class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        # edge cases
        if n == 0:
            return 0
        if n == 1:
            return k
        
        ways = [0]*n #save total ways up to each fence
        ways[0] = k # first fence can choose k colors
        # total up to 2nd fence, same color: k; different color: (k-1)* ways[0]
        ways[1] = k + (k-1)*ways[0]
        
        for i in range(2,n):
            # save total ways up to nth fence
            ways[i] = (k-1)*(ways[i-1] + ways[i-2])
        
        return ways[n-1] # list starting from 0

'''
Time complexity: O(n)
Space complexity: O(n) since save a result for each fence
'''
        
        