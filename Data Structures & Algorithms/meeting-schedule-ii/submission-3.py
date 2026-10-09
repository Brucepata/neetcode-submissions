"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # 0 5 15 start
        # 10 20 40 end
        # 0 started with 10 end counter 1
        # can we start 5 counter 2 
        # when start is greater than end, 
        # move end to next. now end is 20 and counter 1
        # move 15  counter 2
        # move 
        start_sorted = sorted([interval.start for interval in intervals])
        end_sorted = sorted([interval.end for interval in intervals])

        print(start_sorted)




