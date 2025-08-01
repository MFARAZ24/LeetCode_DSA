class MyStack:

    def __init__(self):
        self.Mystack = deque()
        

    def push(self, x: int) -> None:
        self.Mystack.append(x)
        

    def pop(self) -> int:
        return self.Mystack.pop()
        

    def top(self) -> int:
        return self.Mystack[-1]
        

    def empty(self) -> bool:
        if not self.Mystack:
            return True
        else:
            return False

        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()