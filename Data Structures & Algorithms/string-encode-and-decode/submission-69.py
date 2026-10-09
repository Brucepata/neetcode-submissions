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
                print("cur num tracker value is: ", num_tracker)
                num_tracker += 1
            num_len = num_tracker - si
            str_len = int(s[si:num_tracker])

            if str_len == 0:
                output.appned("")
                si += 1
                continue
            print("num tracker after is: ", num_tracker)
            print("str_len is: ", str_len)

            print("appending now is: ", s[si:si+str_len+1])
            output.append(s[si + num_len:si+str_len+1])
            si = si + str_len + 1
        
        return output




        
