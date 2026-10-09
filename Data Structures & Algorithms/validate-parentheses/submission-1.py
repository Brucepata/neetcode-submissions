class Solution:
    def isValid(self, s: str) -> bool:
        ps_stack = []
        dic = {"}":"{", "]":"[", ")":"("}
        for char in s:
            if char in ["{", "[", "("]:
                ps_stack.append(char)
            else:
                if not ps_stack:
                    return False
                else:
                    popped = ps_stack.pop()
                    if dic[char] != popped:
                        return False
        return True


