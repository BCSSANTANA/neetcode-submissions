import math

class MinStack:

    def __init__(self):
        self.stack = []
        self.m = math.inf
        self.s = 0
        

    def push(self, val: int) -> None:
        if val < self.m:
            self.m = val
        self.stack.append(val)
        self.s += 1
        

    def pop(self) -> None:
        elem = self.stack.pop()
        self.s -= 1
        if elem == self.m:
            if self.s == 0:
                self.m = math.inf
            else:
                self.m = min(self.stack)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.m

