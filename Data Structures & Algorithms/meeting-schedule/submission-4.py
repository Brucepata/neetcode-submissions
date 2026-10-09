"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        
        sorted_int = sorted(intervals, key=lambda x:x.start)

        prev_start = intervals[0].start
        prev_end = intervals[0].end

        for interval in sorted_int:
            if interval[0].end < prev_end:
                return False
            else:
                prev_end = max(interval[1], prev_end)
        
        return True

