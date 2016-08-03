# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2

@author: Xiang Li
"""

'''
Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?


## to find the middle node of a linked list
set two pointers slow and fast
* slow = traverse 1 step each time
* fast = traverse 2 step each time

* for total event #node in the linked list: 
    fast.next is null, slow is the middile node
* for total odd #node in the linked list:
    fast.next.next is null and fast.next is not null, slow is the middle node

## to reverse linked list
original: 1->2->3
reverse: 3->2->1->Null
algorithm: set current.next as previous node, change current to current
 
next = current.next
current.next = previous
previous = current
current = next

## for this question

# method 1: time complexity O(n), space complexity O(n)
traverse each node and save to an array, and compare nodes from beginning of 
linked list and backward order of array

# method 2: time complexity O(n), space complexity O(1)
reverse first half of the linked list nodes and compare with the 2nd half
reverse until fast pointer reverse whole list (until fast.next is Null)

** odd case: fast.next is Null and fast is not Null
** even case: fast.next is Null and fast is Null

reverse half linked list. no need slow pointer here

not storing anything so space complexity O(1)
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # set fast pointers
        fast = head
        
        prev = None
        current = head
        while fast and fast.next:
            fast = fast.next.next
            
            # reverse nodes
            next = current.next
            current.next = prev
            prev = current
            current = next
            
            # other way to do the revrse
            # current.next, prev, current = prev, current, current.next
            
            
        # assign reverse half head node
        reverse = prev
        
        if fast:
            # if odd case, 2nd half starts with current.next node
            second = current.next
        else:
            second = current
        
        while second:
            if reverse.val != second.val:
                return False
            
            reverse = reverse.next
            second = second.next
            
        return True
        
        
        