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
        # because we want grab in prefix int.
        # I think it is possible with just one pointer but
        # it will be just easier with 2 pointers. 

        while(l < len(s)):
            r = l 
            while(s[r] != "#"):
                r +=1
            str_len = int(s[l:r])

            res.append(s[r+1:r + 1 +str_len])
            
            l = r + str_len + 1
        
        return res







        return res
    