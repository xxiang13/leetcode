# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 22:10:19 2015

@author: Shawn like

IDE: Spyder Python 3.4
"""

'''
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?

'''
#%%
def addDigits(num):
        """
        :type num: int
        :rtype: int
        """
        find = False
        
        while not find:
            digits = [int(x) for x in list(str(num))]
            
            if len(digits) > 1:
                find = False
                num = sum(digits)
            else:
                find = True
        return num

#%% Test
addDigits(38)