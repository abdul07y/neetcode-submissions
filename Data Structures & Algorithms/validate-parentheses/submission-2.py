class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            if i == '(':
                stack.append(i)

            if i == '{':
                stack.append(i)

            if i == '[':
                stack.append(i)

            if i == ')':
                if not stack or stack[-1] != '(':
                    return False
                stack.pop()

            if i == '}':
                if not stack or stack[-1] != '{':
                    return False
                stack.pop()

            if i == ']':
                if not stack or stack[-1] != '[':
                    return False
                stack.pop()

        return len(stack) == 0

            