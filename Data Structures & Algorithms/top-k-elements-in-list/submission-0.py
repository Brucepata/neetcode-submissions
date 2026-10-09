class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mos = {}
        counter_heap = []
        heapq.heapify(counter_heap)
        '''
        python heap min heap by default
        sorted by the first element
        Say we have
        {1:1,2:2, 3:3}

        say 1 ,2 ,3 ,5 6, 
        2nd most  = same as 4th least. 
        len(nums)-k + 1


        '''
        for num in nums:
            if num not in mos:
                mos[num] = 1
            else:
                mos[num] += 1
        
        for keys in mos.items():
            heapq.heappush(counter_heap,(mos[keys], keys))
        
        elem = None
        for i in range(len(mos.items()) - k + 1):
            elem = heqpq.heappop(counter_heap)
        
        return elem[1]

        
