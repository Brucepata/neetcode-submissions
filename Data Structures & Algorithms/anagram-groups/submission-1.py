class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_dict = {}
        
        for item in strs:
            if item.sort() not in ana_dict:
                ana_dict[item] = [item]
            else:
                ana_dict[item].append(item)
            
        return ana_dict.values()
        
