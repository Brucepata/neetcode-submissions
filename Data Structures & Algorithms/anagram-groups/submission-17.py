class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_dict = {}

        for strr in strs:
            srted = "".join(sorted(strr))

            if srted not in ana_dict:
                ana_dict[srted] = [strr]
            else:
                ana_dict[srted].append(strr)
        
        return list(ana_dict.values())