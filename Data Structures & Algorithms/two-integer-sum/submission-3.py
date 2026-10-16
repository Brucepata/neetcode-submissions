# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         sum_dic = dict()
#         for i in range(len(nums)):
#             sum_dic[target-nums[i]] = i

#         print("sum dic is: ", sum_dic) 
#         for i in range(len(nums)):
#             if target - nums[i] in sum_dic and i != sum_dic[target-nums[i]]:
#                 return sorted([i,sum_dic[target-nums[i]]])
#         return []

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_dic = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in sum_dic:
                return [sum_dic[complement], i]

            sum_dic[num] = i

        return []