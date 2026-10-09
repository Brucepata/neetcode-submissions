class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_dict = {}

        answer = []
        
        for item in strs:
            sorted_item = ''.join(sorted(item))
            if sorted_item not in ana_dict:
                ana_dict[sorted_item] = [item]
            else:
                ana_dict[sorted_item].append(item)
            
        for key, value in ana_dict.items():
            answer.append(value)
    
        return answer

        
