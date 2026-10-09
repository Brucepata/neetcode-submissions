class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = set()

        def find_permutations(i, cur):
            cur.append(nums[i])
            res.add(cur.copy())
            cur.pop()
            find_permutations(i+1, cur)
        
        find_permutations(0, [])

        return res

