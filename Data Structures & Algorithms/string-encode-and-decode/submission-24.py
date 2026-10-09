class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        # #4word#5wordd ...
        for word in strs:
            encoded_str += "#" + str(len(word)) + word
        
        return encoded_str


    def decode(self, s: str) -> List[str]:
        ans = []

        l = 0 
        r = len(s)-1

        while(l <= r):
            if s[l] == "#":
                word_len = int(s[l+1:l+1])
                word_to_add = s[l+2: l+2+word_len]
                ans.append(word_to_add)

                l = l+2+word_len+1
                continue
            l += 1
        
        return ans

