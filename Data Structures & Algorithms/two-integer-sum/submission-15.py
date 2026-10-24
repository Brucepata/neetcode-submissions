class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
            say we save the remainders
            3,4,5,6 case
            then

            0, 4
            1, 3
            2, 2
            3, 1
        '''
        remain_dict = dict()

        for i in range(len(nums)):
            remainder = target - nums[i]

            if remainder in remain_dict:
                return [ remain_dict[remainder], i]
            
            remain_dict[nums[i]] = i

        return  []
        


