class Solution:
    def fib(self, n: int) -> int:
        
        # base case
        if n==0 :
            return 0
        
        if n==1 :
            return 1

        # fib(3) = fib(2) + fib(1)
        #        = 1+1+1, 1+2, 2+1 = 3
        # 2로 끝나는 경우 : 1+2
        # 1로 끝나는 경우 : 1+1+1, 2+1
        return self.fib(n-1) + self.fib(n-2)

        