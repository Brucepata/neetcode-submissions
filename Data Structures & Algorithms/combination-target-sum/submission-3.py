class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def dfs(i, cur, total):
            cur.append(nums[i])
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(nums) or total > target:
                return
            # [2]
            dfs(i, cur, total + num[i] ) # dfs(0, [2], )
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)

        return res 
            
