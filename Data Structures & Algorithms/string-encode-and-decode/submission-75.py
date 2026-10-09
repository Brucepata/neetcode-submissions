class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        HELLO, WORLD
        len(HELLO) = 5
        len(WORLD) = 5
        HELLO!5WORLD!%

        vs

        5#HELLO5#WORLD
        vs
        #5HELLO -> this could work but requires more application code logic
        as we have to stop until we hit the alphabet. 
        Instead the first approach we can check for "#" 
        """
        encoded = ""

        for st in strs:
            st_len = len(st)
            encoded = encoded + str(st_len) + "#" + st

        return encoded

    def decode(self, s: str) -> List[str]:
        print('encoded is : ', s)
        decoded = []
        l = 0 
        while(l < len(s)):
            num_str = ""
            while (l != "#"):
                num_str += s[l]
                l += 1
            str_len = int(num_str)
            decoded.append(s[l+1:l + 1 + num_str])
            l += 1 

        return decoded
            





