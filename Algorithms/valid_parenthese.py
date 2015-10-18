# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 20:48:03 2015

@author: Shawn Li

IDE: Syder python 3.4
"""

'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

The brackets must close in the correct order, 
"()" and "()[]{}" are all valid but "(]" and "([)]" are not.

'''

'''
Note:
The approach of the prob is using the definiton of Stack. 
create a check list, keep adding open parentheses until meet close parentheses, 
check if it is in pair of last one added in the check list. If it is, pop last element of check list;
otherwise, return False. 

But two additional cases need to be considered:
1. checkList, which containing only open parenthese, is empty after pop all matching cases, 
but there is/are close parenthese(s). => return False. Example: [])
2. Similar idea but happends on open parenthese side => return False. Example: ([]
'''
def isValid(s):
        """
        :type s: str
        :rtype: bool
        """
        
        openP = ['(','[','{']
        closeP = [')',']','}']
        
        check = []
        for i in range(len(s)):
            if s[i] in openP:
                check.append(s[i])
                
            if s[i] in closeP:
                if len(check) != 0:
                    if openP.index(check.pop()) != closeP.index(s[i]):
                        return False
                else:
                    return False
                    
        return len(check) == 0

#%%Test
s="{()}"
isValid(s)