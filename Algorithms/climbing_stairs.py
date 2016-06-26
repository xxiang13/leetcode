# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 18:44:40 2016

@author: apple
"""

'''

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?
'''

'''
Think like a decision treen starting at n, next level can take 1 step (n-1) or 
2 steps (n-2). Continue branching out until reach either 0 or 1, then the number
of leaves is the number of distinct ways to get to n with 1 or 2 steps.

Using recursion method, base case is n is either 1 or 0 would give 1 way left.
save number of ways of each number of stairs (n) in a dictionary,
so meet the same case, no need to run
'''

class Solution(object):
    
    def __init__(self):
        self.stairs = {}
        
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n <= 1:
            self.stairs[n] = self.stairs.get(n,1)
            return 1
        
        if n in self.stairs:
            #if # stairs seen before, return saved result
            return self.stairs[n]
        else:
            # save result in a dic
            self.stairs[n] = self.climbStairs(n-1) + self.climbStairs(n-2)            
            return self.stairs[n]
        
        
        
        
#%% test
if __name__ == "__main__":
    test = Solution()
    cases = {0: 1,
             1: 1,
             2: 2,
             3: 3,
             4: 5,
             5: 8}
    for case in cases:
        assert test.climbStairs(case) == cases[case]