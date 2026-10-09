class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_dict = dict()
        for st in strs:
            st_sorted = ''.join(sorted(st))
            if st_sorted in ana_dict:
                ana_dict[st_sorted].append(st)
            else:
                ana_dict[st_sorted] = [st]
        
        return ana_dict.values()