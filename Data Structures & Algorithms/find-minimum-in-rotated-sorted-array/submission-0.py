class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        Rotating means:
        [1,2,3,4,5,6] n = 1
        becomes 
        [6,1,2,3,4,5]
            How do we know wher the minimum is?
        Edge case, 
        What if the minimun is on the right 
        Stritly increasing numbers
        in the case of [4,5,6,1,2,3]
        mid = (5 + 0 )//2 = 2 , -> 6

        when to search right:
         if nums[l] < nums[r]:

        when to search left:

        '''
        print("num is : ", nums)

        l = 0
        r = len(nums)-1
    
        while(l < r):
            mid = (l + r ) // 2
            mid_val = nums[mid] 
            left_val = nums[l]
            right_val = nums[r]
            if mid_val > right_val:
                # search right 
                l = mid + 1 
            else:
                r = mid - 1
        print(mid)
        return nums[mid] 

            















        