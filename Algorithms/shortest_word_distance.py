# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6

@author: Xiang Li
"""

'''
Given a list of words and two words word1 and word2, return the shortest 
distance between these two words in the list.

For example, Assume words = ["practice", "makes", "perfect", "coding", "makes"]

Given word1 = “coding”, word2 = “practice”, return 3. Given word1 = "makes", 
word2 = "coding", return 1.

Note: You may assume that word1 does not equal to word2, and word1 and word2 
are both in the list.
'''

'''
Clarify: if duplicated words in the list? Here assume YES

Solution:
two ponters: one static, one_word, and one dynamic, i
pointer i iterage the whole list, each time check if elements == any of give words
if yes, set pointer one_word = the index, ifduplicated word showing up, 
update the pointer one_world until i meets the other word, save the shortest
world length so far and set one_word pointer to the other word. Keep updating
the shortest distance until i iterage whole list.
'''
 
class Solution:
    def shortestDistance(self, words, word1, word2):
        '''
        Inpute: words, String list
                word1, String
                word2, String
        Return: integer
        '''
        
        if len(words) <= 1:
            return 0
            
        one_word = 0
        word_tocheck = [word1, word2]
        shortest_distance = len(words)
        word_checked = None
        
        for i in range(len(words)):
            if words[i]== word1 and not word_checked:      
                one_word = i
                word_checked = word1
            
            if words[i]== word2 and not word_checked:      
                one_word = i
                word_checked = word2
            
            if words[i] in word_tocheck:
                if words[i] == word_checked:
                    one_word = i
                    
                else:
                    shortest_distance = min(shortest_distance,i - one_word)
                    one_word = i
                    word_checked = words[i]
                    
        return shortest_distance

#%% test
if __name__ == '__main__':
    test = Solution()
    
    words = ["practice", "makes", "perfect", "coding", "makes"]
    word1 = "coding"
    word2 = "practice"
    
    test.shortestDistance(words, word1, word2) # 3
    
    word1 = "makes"
    word2 = "coding"
    
    test.shortestDistance(words, word1, word2) # 1
                