class Solution:
    def __init__(self):
        self.encodedStrings = {}

    def encode(self, strs: List[str]) -> str:
        encoding_connector = "!%"
        encoded_string = ""
        for st in strs:
            encoded_string = encoded_string+st+encoding_connector
        print("encoded string is: ", encoded_string)
        
        self.encodedStrings[encoded_string] = strs

    def decode(self, s: str) -> List[str]:
        if s not in self.encodedStrings:
            return None
        return self.encodedStrings[s].split("!%")