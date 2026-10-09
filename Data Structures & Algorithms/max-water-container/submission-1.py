class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        Area = min(l, r)* (r-l)
        '''
        if not heights:
            return 0

        cur_max = 0
        
        l = 0 
        r = len(heights)-1


        while( l < r ):
            cur_max = max(cur_max, min(heights[l], heights[r]) * (r -l))

            if l < r:
                l += 1
            else:
                r -= 1
        
        return cur_max


        