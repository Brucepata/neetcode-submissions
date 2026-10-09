"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        sorted_interval = sorted(intervals, key=lambda x : x[0])

        num_days = 1

        prev_max = sorted_interval[0][1]

        for i in range(1, len(sorted_intervals)):

            if sorted_intervals[i][0] < prev_max:
                num_days += 1
            
            prev_max = sorted_intervals[i][1]
        
        return num_days
