# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27

@author: Xiang Li
"""

'''

Merge two sorted linked lists and return it as a new list. 
The new list should be made by splicing together the nodes 
of the first two lists.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        

#%%

'''
create a new node with any value. going to loop, append smaller node in the overall sorted list
until run out of one of the lists (l1 or l2 is none). append rest of sorted list 
to the overall sorted list, return first.next by excluding first node

worst case: need to compare each element, so time complexity O(n), space O(1)
'''
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        first = None
        current = None
        
        if not l1:
            return l2
        
        if not l2:
            return l1
        
        
        first = ListNode(0)
        current = first
        
        while l1 and l2:
            if l1.val > l2.val:
                current.next = l2
                l2 = l2.next

            else:
                current.next = l1
                l1 = l1.next
            current = current.next
        
        if l1:
            current.next = l1
        
        if l2:
            current.next = l2
                
        return first.next
        
    def printList(self,ls_node):
        s = str(ls_node.val)
        ls_node = ls_node.next
        while ls_node:
            s = s + " -> " + str(ls_node.val)
            ls_node = ls_node.next
        print(s)
        
#%% test
test = Solution()

l1_0 = ListNode(3)
l1_1 = ListNode(10)
l1_2 = ListNode(20)
    
l1_0.next = l1_1
l1_1.next = l1_2
    
l2_0 = ListNode(1)
l2_1 = ListNode(2)
l2_2 = ListNode(3)
l2_3 = ListNode(15)
l2_4 = ListNode(30)
l2_5 = ListNode(35)
    
l2_0.next = l2_1
l2_1.next = l2_2
l2_2.next = l2_3
l2_3.next = l2_4
l2_4.next = l2_5
    
test.printList(l1_0)
test.printList(l2_0)
    
a = test.mergeTwoLists(l1_0,l2_0)

test.printList(a)

