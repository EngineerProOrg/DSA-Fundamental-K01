# https://leetcode.com/problems/valid-parentheses
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for x in s:
            if x in ['(', '[', '{']:
                stack.append(x)
            else:
                if not stack: # stack is empty
                    return False
                last_ele = stack.pop()
                if not self.match(last_ele, x):
                    return False

        return len(stack) == 0

    def match(self, x, y):
        return (x == '(' and y == ')') or \
                (x == '[' and y == ']') or \
                (x == '{' and y == '}')
