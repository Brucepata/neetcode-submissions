class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        ana_dict = {}
        first_word_seen = len(s)

        for char in s:
            if char not in ana_dict:
                ana_dict[char] =1
            else:
                ana_dict[char] += 1
        
        for char in t:
            if char in ana_dict and ana_dict[char] > 0:
                first_word_seen -= 1
        
        return True if first_word_seen == 0 else False
        