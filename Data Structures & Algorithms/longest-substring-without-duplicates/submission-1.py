class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0 
        if len(s) < 1:
            return max_len
        l = 0
        r = 0 
        char_counter = dict()
        while(r < len(s)):
            if s[r] not in char_counter or not char_counter[s[r]]:
                char_counter[s[r]] = True
            else:
                # s[r] in char_counter
                while(s[l] != s[r]):
                    char_counter[s[l]] = False
                    l += 1
                char_counter[s[l]] = False
                l += 1
                char_counter[s[r]] = True
            max_len = max(max_len, (r-l)+1)
            r += 1
    
        return max_len
                

