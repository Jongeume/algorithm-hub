from collections import deque


class MyStack:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)
        print(self.queue)

    def pop(self) -> int:
        n = len(self.queue)
        while n > 1:
            self.queue.append(self.queue.popleft())   
            n-=1
        return self.queue.popleft()

    def top(self) -> int:
        n = len(self.queue)
        peek = 0
        while n > 0:
            peek = self.queue.popleft()
            self.queue.append(peek)
            n-=1
        return peek

    def empty(self) -> bool:
        return False if self.queue else True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()