class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_dict = {}
        for i, num in enumerate(nums):
            if target - num in sum_dict:
                return [i, sum_dict[target-num]]
            else:
                sum_dict[num] = i
        
        return 
