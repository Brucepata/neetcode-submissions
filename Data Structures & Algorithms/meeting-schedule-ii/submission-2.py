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

        sorted_interval = sorted(intervals, key=lambda x : x.start)

        num_days = 1

        prev_max = sorted_interval[0].end

        for i in range(1, len(sorted_interval)):

            if sorted_interval[i].start < prev_max:
                num_days += 1
            
            prev_max = sorted_interval[i].end
        
        return num_days
