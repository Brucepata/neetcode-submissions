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

        num_room = 0 
        res = 0 
        s, e = 0 , 0 

        start_sorted = sorted([interval.start for interval in intervals])
        end_sorted = sorted([interval.end for interval in intervals])

        while(s <= len(start_sorted)-1):

            if start_sorted[s] < end_sorted[e]:
                num_room += 1
                res = max(num_room, res)
            else:
                num_room -= 1
        
        return res






