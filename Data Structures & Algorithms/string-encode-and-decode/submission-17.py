class Solution:
    
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s))+ "#" + s
        
        return res

    def decode(self, s: str) -> List[str]:

        res = []
        l = 0 
        # do we need two pointers here?
        while(l < len(s)):
            r = l 
            while(s[r] != "#"):
                r +=1
            str_len = int(s[l:r])

            print("str len is : ", str_len)
            res.append(s[r+1:r + 1 +str_len])
            
            l = r + str_len + 1
        
        return res







        return res
    