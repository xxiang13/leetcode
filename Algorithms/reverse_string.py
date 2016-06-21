# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20

@author: Xiang Li
"""

'''
Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".
'''

#%% method 1: too slow O(n)
def reverseString(s):
    """
    :type s: str
    :rtype: str
    """
    
    reverse = ''
    while s:
        reverse += s[-1]
        s = s[:-1]
    return reverse


#%% method 2: 
'''
Slicing syntax has supported an optional third ``step'' or ``stride'' argument
Negative values also work to make a copy of the same list in reverse order
'''

def reverseString(s):
    """
    :type s: str
    :rtype: str
    """
    return s[::-1]
#%% test
s = "hello"
s1 = "hello world"
reverseString(s)
reverseString(s1)