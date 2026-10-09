class Solution:

    def encode(self, strs: List[str]) -> str:
        #4neet#4code#4love#4you
        encoded = ""

        for elem in strs:
            encoded = encoded + "#" + str(len(elem)) + elem
        
        print("encoded is: ", encoded)
        return encoded


    def decode(self, s: str) -> List[str]:
        # say apple is length 5, #5apple
        # at 1, you add 5, index is at 6, if you do 1:6 you will get apple 
        output = []
        si = 0

        if s[si] != "#":
            return []

        while si != len(s):
            si += 1
            num_tracker = si
            while(s[num_tracker].isnumeric()):
                num_tracker += 1
            decoded_str = s[si:num_tracker]
            output.append(decoded_str)
            si = si + len(decoded_str) + 1
        
        return output




        
