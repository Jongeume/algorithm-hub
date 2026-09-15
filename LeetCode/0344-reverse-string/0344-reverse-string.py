class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # 기존의 투포인터 방식을 응용
        def f(left, right):
            # 길이 짝수 : h i g h (left > right)
            # 1 : h i g h, left: 0, right: 3
            # 2 : h g i h, left: 1, right: 2
            # 3 : left: 2, right: 1 ==> return
            

            # 길이 홀수 : h e l l o  (left = right)
            # 1 : o e l l h, left: 0, right: 4
            # 2 : o l l e h, left: 1, right: 3
            # 3 : o l l e h, left: 2, right: 2 ==> return
            if left >= right:
                return
            s[left], s[right] = s[right], s[left]
            f(left + 1, right -1)
        
        f(0, len(s)-1)