class Solution:
    def climbStairs(self, n: int) -> int:
        # 첫번째 그냥 재귀 방식
        # 한번에 1 or 2칸 씩 오를 수 있다.
        # n-1, n-2

        # base case
        # if n==1:
        #     return 1
        # if n==2:
        #     return 2

        # return self.climbStairs(n-1) + self.climbStairs(n-2)

        # 두번째 메모이제이션
        # 딕셔너리로 값 저장
        # memo = {}

        # def f(n):
        #     if n <= 2:
        #         return n
        #     if n in memo:
        #         return memo[n]
        #     memo[n] = f(n - 1) + f(n - 2)
        #     return memo[n]

        # return f(n)

        # 세번째 DP
        if n <= 2:
            return n
        dp = [0] * (n+1)
        dp[1], dp[2] = 1, 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]