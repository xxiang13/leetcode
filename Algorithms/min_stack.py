# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5

@author: Xiang Li
"""

'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
'''

'''
have 2 stacks, one for storing min values
'''

class MinStack(object):
    
    def __init__(self):
        # @param x, an integer
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        # @return an integer
        self.stack1.append(x)
        if len(self.stack2) == 0 or x <= self.stack2[-1]:
            self.stack2.append(x)

    def pop(self):
        # @return nothing
        if self.stack1:
            top = self.stack1[-1]
            self.stack1.pop()
            if top == self.stack2[-1]:
                self.stack2.pop()
        
    def top(self):
        # @return an integer
        return self.stack1[-1]

    def getMin(self):
        # @return an integer
        return self.stack2[-1]
                
        
        
        
        
#%%

minStack = MinStack();
minStack.push(-2);
print(minStack.getMin());# Returns  -2
minStack.push(0);
minStack.push(-3);
print(minStack.getMin());# Returns -3.
minStack.pop();
minStack.top();# Returns 0.
print(minStack.getMin());# Returns -2.
minStack.pop();
minStack.pop();
minStack.pop();
print(minStack.getMin());
