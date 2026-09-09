class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []

        ## 1. 스택에 하나씩 넣다가
        ## 2. # 들어가는 순간 stack.pop()

        for w in s:
            if w == "#" :
                if stack1:
                    stack1.pop()
            else :
                stack1.append(w)
      
        for w in t:
            if w == "#" :
                if stack2:
                    stack2.pop()
            else:
                stack2.append(w) 

        print(stack1)
        print(stack2)

        return True if stack1 == stack2 else False

        