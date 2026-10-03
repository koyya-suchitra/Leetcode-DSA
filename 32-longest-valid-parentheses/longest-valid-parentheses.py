class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]  # base index
        max_len = 0
        
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            else:  # ch == ')'
                stack.pop()
                if not stack:
                    stack.append(i)  # reset base
                else:
                    max_len = max(max_len, i - stack[-1])
        
        return max_len
