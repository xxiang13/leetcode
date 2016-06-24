# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23

@author: Xiang Li
"""

'''
Given a sorted linked list, delete all duplicates such 
that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
'''

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None
         

'''
since it's a sorted linked list, duplicated node would come along
check node.next if value is same, update next linked node
update node to check when value not same
since need to check each node, time efficiency O(n)
'''

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
            
        current_node = head
        while current_node.next:
                if current_node.next.val == current_node.val:
                    current_node.next = current_node.next.next
                else:
                    current_node = current_node.next
            
        return head
        
        
#%% sep up linked list
a = ListNode(1)
b = ListNode(1)
c = ListNode(1)
d = ListNode(3)
e = ListNode(3)

a.next = b
b.next = c
#c.next = d
#d.next = e
#%% test
test = Solution()
test.deleteDuplicates(a)

current = a
while current:
    print(current.val)
    current = current.next