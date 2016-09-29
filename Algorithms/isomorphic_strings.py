# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 20:54:20 2016

@author: apple
"""
'''
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

Note:
You may assume both s and t have the same length.
'''

'''
method 1
in each string, same char assign same number
if two strings have a same pattern => isomorphic
Worse case: if strings are isomorphic, need to check all chars
time efficiency: O(n)
'''
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if len(s) != len(t):
            return False
            
        d1 = {}
        d2 = {}
        for i in range(len(s)):
            d1[s[i]] = d1.get(s[i],i)
            d2[t[i]] = d2.get(t[i],i)
            
            if d1[s[i]] != d2[t[i]]:
                return False
        
        return True

#%%
cases = {("egg","add"):True,
         ("foo","bar"):False,
         ("paper","title"):True,
         ("ab","aa"): False}
    
for case in cases:
    assert test.isIsomorphic(*case) == cases[case]