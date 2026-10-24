class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_set = dict()
        t_set = dict()

        for sv in s:
            if sv not in s_set:
                s_set[sv] = 1
            else:
                s_set[sv] +=1

        for sv in t:
            if sv not in t_set:
                t_set[sv] = 1
            else:
                t_set[sv] +=1

        
        return s_set == t_set