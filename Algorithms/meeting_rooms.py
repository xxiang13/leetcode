# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 21:43:08 2016

@author: apple
"""

'''
Given an array of meeting time intervals consisting of start and end times 
[[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

For example, Given [[0, 30],[5, 10],[15, 20]], return false.
'''

'''
Solution: sort staring time, if end time after less than starting time before,
it means two meeting overlaped -> return False. Check until end, if no overlaps,
return True
'''

class Solution:
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        intervals.sort(key = lambda x: x[0])
        print(len(intervals))
        
        for i in range(len(intervals)-1):
            if intervals[i][1] > intervals[i+1][0]:
                return False
        
        return True

#%% test
test = Solution()
test.canAttendMeetings([[0, 30],[5, 10],[15, 20]])