# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6

@author: Xiang Li
"""

'''
Write a function that takes a string as input and reverse 
only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".
'''

'''
staring from beginning and end to check vowels same time,
swap when both sides are vowels until left index goes over 
right one. Need to check each element, time complexity O(n)
'''

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        vowels = {"a","e","i","o","u","A","E","I","O","U"}
        
        left = 0
        right = len(s)-1
        
        while left < right:
            if s[left] not in vowels:
                left += 1

            if s[right] not in vowels:
                right -= 1
                
            if s[left] in vowels and s[right] in vowels:
                s[left],s[right] = s[right],s[left]
                left += 1
                right -= 1
                
        return ''.join(s)
                
#%% test
if __name__ == "__main__":
    
    test = Solution()
    cases = {"hello": "holle", "leetcode": "leotcede", "m": "m", "qq": "qq", "soy": "soy", 'Aa':'aA'}
    
    for word in cases:
        assert test.reverseVowels(word) == cases[word]
            
    