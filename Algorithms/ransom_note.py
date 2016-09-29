# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10

@author: Xiang Li
"""

'''
Given an arbitrary ransom note string and another string containing letters
from all the magazines, write a function that will return true if the ransom
note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false 
canConstruct("aa", "ab") -> false 
canConstruct("aa", "aab") -> true
'''

'''
Solution:
1. naive approach: nested for loops, for each element in rannsomNone and check 
it it's in magazine. Time complexity: O(n^2): n elements in ransomeNote search n elements
in magazine
 
 
2. Better approach: iterate magzine, save each letter as key and num of time apperances
in magzine as value in a hash table. Then, iterage ransomNote, if it not in hash table,
return true; if in hash table and value != 0, value -= 1 until end of ransomeNote
if in hash table and value == 0, return false. 
Time complexity: O(n). Space complexity: O(n)

'''

# better apprach
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        #edge cases
        if not ransomNote:
            return True
        
        if not magazine:
            return False
            
        if len(ransomNote) > len(magazine):
            return False
            
        # assign letters in magazine to hash table
        m_letters = {}
        for e in magazine:
            m_letters[e] = m_letters.get(e,0) + 1
        
        for i in ransomNote:
            if m_letters.get(i,0) == 0:
                return False
            else:
                m_letters[i] -= 1
        
        return True
        
#%%test
if __name__ == '__main__':
    test = Solution()
    
    test.canConstruct("a", "b")     # -> false
    test.canConstruct("aa", "ab")   # -> false
    test.canConstruct("aa", "aab")  # -> true       
            