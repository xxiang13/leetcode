# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 23:33:39 2016

@author: apple
"""


'''
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

-1 : My number is lower
 1 : My number is higher
 0 : Congrats! You got it!
Example:
n = 10, I pick 6.

Return 6.
'''

'''
Solution: Binary search

and update either lower or upper bound since mid always = (upper+lower)/2
'''
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

def guess(num):
    '''
    @param num, your guess
    @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
    '''
    g = 24
    if num == g:
        return 0
    elif g < num:
        return -1
    else:
        return 1
        
        
class Solution(object):

    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        lower,upper = 1,n

        while lower <= upper:
            mid = (upper+lower)//2
            if guess(mid) <= 0:
                upper = mid -1
            else:
                lower = mid + 1
            
        return lower

#%%
if __name__ == '__main__':
    
    test = Solution()
    test.guessNumber(100)