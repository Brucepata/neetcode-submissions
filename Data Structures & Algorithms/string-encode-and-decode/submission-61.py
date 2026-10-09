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

        while(r < len(s)):
            r = l 

            while(r != "#"):
                r += 1

            str_len = int(s[l:r])

            l = r + 1

            for i in range(str_len+1):
                r += 1
            
            decoded.append(s[l:r])

            l = r + 1 
        
        return decoded







