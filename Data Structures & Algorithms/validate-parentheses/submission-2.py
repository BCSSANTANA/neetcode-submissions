class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = ["(", "{", "["]
        closing = [")", "}", "]"]
        for c in s:
            if c in opening:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                i = closing.index(c)
                elem = stack.pop()
                if elem != opening[i]:
                    return False
        return True if len(stack) == 0 else False