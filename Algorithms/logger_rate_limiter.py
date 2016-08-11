# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9

@author: Xiang Li
"""

'''
Design a logger system that receive stream of messages along with its timestamps,
 each message should be printed if and only if it is not printed in the last 10 seconds.

Given a message and a timestamp (in seconds granularity), return true if the message
 should be printed in the given timestamp, otherwise returns false.

It is possible that several messages arrive roughly at the same time.

Example:

Logger logger = new Logger();

// logging string "foo" at timestamp 1
logger.shouldPrintMessage(1, "foo"); returns true; 

// logging string "bar" at timestamp 2
logger.shouldPrintMessage(2,"bar"); returns true;

// logging string "foo" at timestamp 3
logger.shouldPrintMessage(3,"foo"); returns false;

// logging string "bar" at timestamp 8
logger.shouldPrintMessage(8,"bar"); returns false;

// logging string "foo" at timestamp 10
logger.shouldPrintMessage(10,"foo"); returns false;

// logging string "foo" at timestamp 11
logger.shouldPrintMessage(11,"foo"); returns true;


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
'''

'''
Solution: Hash table
Use hash table to save printed message {msg:time} in previous 10 seconds
check new message if in the table:
if no, print msg and save it into the table
if yes, print msg and update time for the table
'''
class Logger(object):
    def __init__(self):
        """
        Initialize data structure here.
        """
        self.mp = {}
        
    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, 
        otherwise returns false. The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if message not in self.mp:
            self.mp[message] = timestamp
            return True
        else:
            if timestamp - self.mp[message] >= 10:
                self.mp[message] = timestamp
                return True
        
        return False
        
#%%test
test = Logger()
test.shouldPrintMessage(1,"a") #True
test.shouldPrintMessage(2,"b") #True
test.shouldPrintMessage(1,"c") #True
test.shouldPrintMessage(5,"a") #False
test.shouldPrintMessage(6,"d") #True
test.shouldPrintMessage(9,"c") #False
test.shouldPrintMessage(20,"d") #True
test.shouldPrintMessage(21,"a") #True
test.shouldPrintMessage(22,"b") #True
