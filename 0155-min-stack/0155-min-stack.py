class MinStack:

    def __init__(self):
        self.stack = []
        self.Minstack = []
                

    def push(self, val: int,) -> None:
        self.stack.append(val)
        if len(self.Minstack) == 0 or val<=self.Minstack[-1]:
            self.Minstack.append(val)
            

    def pop(self) -> None:

        if len(self.stack)!=0:
            if self.stack[-1] == self.Minstack[-1]:
                self.Minstack.pop()
            return self.stack.pop()
        else:
            return None
        

    def top(self) -> int:
        if len(self.stack)!=0:
            return self.stack[-1]
        else:
            return None   
        

    def getMin(self) -> int:
        if len(self.Minstack)!=0:
            return self.Minstack[-1]
        else:
            return None
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()