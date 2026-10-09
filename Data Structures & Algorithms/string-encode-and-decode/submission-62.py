class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_st = ""

        for st in strs:
            encoded_st = str(len(st)) + "#" + st
        return encoded_st

    def decode(self, s: str) -> List[str]:
        # 4#neet4#code4#love4#you
        l = 0
        r = 0

        decoded = []

        while(l < len(s)):
            while s[r] != "#":
                r += 1
                # now at # 
            str_len = int(s[l:r])
            l = r + 1
            decoded_str = s[l:l+str_len]

            l = l + str_len
            r = l
            
        
        return decoded







