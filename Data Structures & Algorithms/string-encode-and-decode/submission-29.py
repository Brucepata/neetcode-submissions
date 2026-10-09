class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        encoded_str = ""
        # #4word#5wordd ...
        for word in strs:
            encoded_str += "#" + str(len(word)) + word
        
        return encoded_str


    def decode(self, s: str) -> List[str]:

        ans = []

        l = 0 
        r = len(s)-1

        print(s)

        while(l <= r):
            if s[l] == "#":
                g = l + 1
                
                while(s[g] in "0123456789"):
                    g += 1
                
                word_len = int(s[l+1:g])

                print("word len is ", word_len)
                word_to_add = s[l+2: l+2+word_len]
                ans.append(word_to_add)

                l = l+2+word_len
                continue
            l += 1
        
        return ans

