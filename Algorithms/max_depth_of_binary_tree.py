# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21

@author: Xiang Li
"""

'''
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest
 path from the root node down to the farthest leaf node.
'''

# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

#%% method 1
'''
use BFS to find the level of the tree 
longest path = level + 1
tracking number of parents which informs
where is a next level
if number of parents = 0, no next level
time: O(n)
'''
def maxDepth(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if not root:
        return 0
        
    queue = [root]
    num_parents = len(queue)
    level = 1
    while queue:
        i = 1
        while i <= num_parents:
            node = queue.pop(0)
            
            if node.left:
                queue.append(node.left)               
            if node.right:
                queue.append(node.right)
                
            i += 1

        num_parents = len(queue)
        if num_parents != 0:
            level += 1
    return level

#%% method 2: use recursion

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:  
            return 0  
        else:  
            return max(self.maxDepth(root.left),self.maxDepth(root.right))+1 

#%% test set up a binary tree
n0 = TreeNode(0)
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)

n0.left = n1
n0.right = n2
n1.left= n3
n1.right = n4
n2.left = n5

maxDepth(None)
        