class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack:
            curr_min = self.minStack[-1]
            if curr_min <= val:
                self.minStack.append(curr_min)
            else:
                self.minStack.append(val)
        else:
            self.minStack.append(val)            


    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
