class Solution:

    def encode(self, strs: List[str]) -> str:
        # #4neet#4code so on..
        encoded_str = ""
        for word in strs:
            encoded_str += "#" + str(len(word)) + word

        print("encoded str is:", encoded_str)
        
        return encoded_str

    def decode(self, s: str) -> List[str]:
        
        l = 0 
        r = len(s)

        res = []

        while(l < r):
            #we will move l to the r + 1 
            # when this goes == r , means that we are out of boudn should end.
            # thus this while loop is good for this case. 
            if s[l] == "#":
                # word exists.
                word_len = int(s[l:r+1])
                res.append(s[l+2:l+2+word_len])

        return res

