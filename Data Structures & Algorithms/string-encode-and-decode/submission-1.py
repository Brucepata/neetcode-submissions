class Solution:

    def encode(self, strs: List[str]) -> str:
        encoding_connector = "!%"
        encoded_string = ""
        for str in strs:
            encoded_string = encoded_string+encoding_connector
        return encoded_string

    def decode(self, s: str) -> List[str]:
        return s.split("!%")