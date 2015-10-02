# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 21:28:58 2015

@author: Shawn Li

IDE: Spyder python 3.4
"""

'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.

'''

import re
#%% pop by index will go though each elements of the list backwards from the end, so not very efficient
def isPalindrome1(s):
        """
        :type s: str
        :rtype: bool
        """
        inputs = list(re.sub('[^a-z0-9]', "", s.lower()))
        
        while len(inputs) > 1:
            if inputs.pop(0) != inputs.pop(-1):
                return False
        
        return True

#%% To improve the efficiency. check from left and right before left index > right index
def isPalindrome2(s):
        """
        :type s: str
        :rtype: bool
        """
        inputs = list(re.sub('[^a-z0-9]', "", s.lower()))
        
        left = 0
        right = len(inputs) - 1
        
        while left < right:
            if inputs[left] == inputs[right]:
                left += 1
                right -= 1
            else: 
                return False
        return True

#%%Test
s= "A man, a plan, a canal: Panamaa"
isPalindrome2(s)

