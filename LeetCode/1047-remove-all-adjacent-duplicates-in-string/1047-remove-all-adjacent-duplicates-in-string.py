class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for word in s:
            if stack and word == stack[-1]: 
                stack.pop()
            else:
                stack.append(word)
            
        

        return ''.join(stack)