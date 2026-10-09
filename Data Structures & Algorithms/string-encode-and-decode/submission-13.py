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
            res.append(s[r+1:str_len])
            
            l = r + 1
        
        return res







        return res
    