class Solution:
    def isValid(self, s: str) -> bool:
        paranthesis_map = {')':'(', '}': '{', ']': '['}
        stack = []

        for char in s:
            
            if char not in paranthesis_map:
                stack.append(char)
            else:
                if stack and stack[-1] == paranthesis_map[char]:
                    stack.pop()
                else:
                    return False
        
        return not stack