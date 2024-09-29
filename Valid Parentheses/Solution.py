class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == "(" or i == "{" or i == "[":
                stack.append(i)
            elif i == ")" or i == "}" or i == "]":
                if not stack:
                    return False
                if (i == ")" and stack[-1] != "(") or (i == "}" and stack[-1] != "{") or (i == "]" and stack[-1] != "["):
                    return False
                stack.pop()
        return len(stack) == 0