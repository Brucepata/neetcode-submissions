class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for word in strs:
            encoded_str += "#" + str(len(word)) + word

        return encoded_str

    def decode(self, s: str) -> List[str]:
        print("Input string:", s)
        
        l = 0 
        r = len(s)

        res = []

        while l < r:

            if s[l] == "#":
                g = l + 1
                print("g is:", g)
                while ((g < r) and (s[g] in "0123456789")):
                    print("g insde is:", g)
                    g += 1
                print("l is :", l)
                print("r is :", r)
                word_len = int(s[l+1:g])
                l = g
                print("word_len is :", word_len)
                word = s[g:g+word_len]
                print("word is: ", word)
                res.append(word)

                print("finally l is :", l)
                print("finally r is :", r)
                l = l + word_len
                
            else:
                l += 1
                print("l izzz: ", l)

        return res
