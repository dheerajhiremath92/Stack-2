class Solution:
    def isValid(self, s: str) -> bool:
        if s is None or len(s) == 0:
            return True
        stack = []
        for i in range(len(s)):
            if s[i] == "[":
                stack.append("]")
            elif s[i] == "(":
                stack.append(")")
            elif s[i] == "{":
                stack.append("}")
            elif (len(stack) == 0 or stack.pop() != s[i]):
                return False
        if len(stack) > 0:
            return False
        return True
