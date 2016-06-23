# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22

@author: Xiang Li
"""

'''

Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, 
return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
'''

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """       
        base = ord("A") - 1
        colname = [ord(char) - base for char in s]
        power = reversed([26**x for x in range(len(s))])
        return sum([a*b for a,b in zip(colname,power)])   
        
#%% test
        
test = Solution()
test.titleToNumber("AAA")
