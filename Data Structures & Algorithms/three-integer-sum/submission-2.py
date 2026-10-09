class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        [-1,0,1,2,-1,-4]
        becomes 
        [-4, -1, -1, 0 , 1, 2]
        '''
        res = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    cur_sum = nums[i] + nums[j] + nums[k]
                    if cur_sum == 0:
                        res.add([i,j,k])
            
        
        return res

        