class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in pairs.values():
                stack.append(char)
            elif char in pairs:      
                if not stack or stack[-1] != pairs[char]:
                    return False
                stack.pop()
            else:
                continue
        return len(stack) == 0 