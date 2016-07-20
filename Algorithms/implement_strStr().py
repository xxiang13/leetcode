# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19

@author: Xiang Li
"""

'''
Implement strStr().

Returns the index of the first occurrence of needle in haystack, 
or -1 if needle is not part of haystack.
'''

'''
iterate until find element in haystack matches needdle[0]
then check if the following substr match needle
'''

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
            
        if len(needle) == 0 and len(haystack) == 0:
            return 0
        elif len(haystack) == 0:
            return -1
        elif len(needle) ==0:
            return 0
            
        for i in range(0,len(haystack)):
            i2 =1
            i1 = 0
            if haystack[i] == needle[0]:
                if len(needle) <= len(haystack[i:]):
                    i1 += i+1
                    find = True
                    #print(len(needle))
                    while find and i2 < len(needle) and i1 < len(haystack):
                        if needle[i2] == haystack[i1]:
                            i2 += 1
                            i1 += 1
                        else:
                            i = i2
                            find = False
                            
                    if find == True:
                        return i
        return -1
                        
                        
        
#%% test
if __name__ == '__main__':
    
    test = Solution()
    case = {('helloei', 'ei'): 5,
            ('hello', 'lop'): -1,
            ('hello', 'hellos'): -1,
            ('helloei', 'l'): 2,
            ('hello', 'hello'): 0,
            ('hello', ''): 0,
            ('', 'a'): -1,
            ('a',''): 0,
            ('a','a'): 0}
        
    for k,v in case.items():
        assert test.strStr(*k) == v
        
test = Solution()
test.strStr("mississippi","issip")