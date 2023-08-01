# https://leetcode.com/problems/valid-parentheses
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for x in s:
            if x in ['(', '[', '{']:  # if x == '(' or x == '[' or x == '{':
                stack.append(x)
            else: # x == ')' or x == ']' or x == '}'
                if not stack: # stack is empty
                    return False
                last_ele = stack.pop()
                if not self.match(last_ele, x):
                    return False

        return len(stack) == 0
        # if len(stack) != 0:
        #    return False
        # else:
        #   return True 

    def match(self, x, y):
        return (x == '(' and y == ')') or \
                (x == '[' and y == ']') or \
                (x == '{' and y == '}')
