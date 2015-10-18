# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 21:45:00 2015

@author: Shawn Li

IDE: Spyder python 3.4
"""

'''
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, 
replace the number by the sum of the squares of its digits, and repeat the process until the number 
equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. 
Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

'''

def isHappy(n):
        """
        :type n: int
        :rtype: bool
        """
        checkList = set() 
        #if n equals to nums in the cycle => will repeat the cycle, won't get 1
        #use checkList to store all values shown
        while n != 1:
            nums = [int(x) for x in str(n)]            
            numSqr = [x*x for x in nums]            
            n = sum(numSqr) 
            if n in checkList:
                return False
            else:
                checkList.add(n)
                
        return True

#%% Test

n = 16
isHappy(n)