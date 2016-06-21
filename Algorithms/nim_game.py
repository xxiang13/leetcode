# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20

@author: Xiang Li
"""

'''
You are playing the following Nim Game with your friend: 
There is a heap of stones on the table, each time one of you take turns to remove 1 to 3 stones. 
The one who removes the last stone will be the winner. You will take the first turn to remove the stones.

Both of you are very clever and have optimal strategies for the game. 
Write a function to determine whether you can win the game given the number of stones in the heap.

For example, if there are 4 stones in the heap, then you will never win the game: 
no matter 1, 2, or 3 stones you remove, the last stone will always be removed by your friend.
'''

'''
staring n = 4, try to find win/loss for each n with possible 3 steps: 1,2,3 and update the result
you would find a pattern is each 4 times, there is a loss 

1  --> T
2  --> T
3  --> T
4  --> Remove 3 --> other player = 1 --> F
       Remove 2 --> other player = 2 --> F
       Remove 1 --> other player = 3 --> F
5  --> Remove 3 --> other player = 2 --> F
       Remove 2 --> other player = 3 --> F
       Remove 1 --> other player = 4 --> T*
6  --> Remove 3 --> other player = 3 --> F
       Remove 2 --> other player = 4 --> T*
       Remove 1 --> other player = 5 --> F
7  --> Remove 3 --> other player = 4 --> T*
       Remove 2 --> other player = 5 --> F
       Remove 1 --> other player = 6 --> F
8  --> Remove 3 --> other player = 5 --> F
       Remove 2 --> other player = 6 --> F
       Remove 1 --> other player = 7 --> F
'''
def canWinNim(n):
    """
    :type n: int
    :rtype: bool
    """
    return n%4 != 0
    
#%% test
canWinNim(5)

    
