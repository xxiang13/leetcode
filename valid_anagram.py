# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 22:36:25 2015

@author: Shawn Li

IDE: Spyder Python 3.4
"""

'''
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

'''

def isAnagram(s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        alphabet1 = {chr(i): 0 for i in range(97,122+1)}
        
        alphabet2 = {chr(i): 0 for i in range(97,122+1)}
        
        if len(t) == len(s):
            for i in range(len(t)):
                alphabet1[t[i]] = 1+ alphabet1[t[i]]
                alphabet2[s[i]] = 1+ alphabet2[s[i]]

            return str(alphabet1.values()) == str(alphabet2.values())
            
        else:
            return False
            
#%%Test
s = "anagram"
t = "nagaram"
isAnagram(s, t)
