class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_max = float("-inf")
        cur_sum = 0 

        for num in nums:
            if num > cur_max:
                cur_max = num
                cur_sum = num
                continue
            cur_sum += num
            cur_max = max(cur_sum, cur_max)
        
        return cur_max
