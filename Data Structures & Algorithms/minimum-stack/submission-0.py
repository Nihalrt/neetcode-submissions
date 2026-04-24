class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            current_val = self.min_stack[-1]
            self.min_stack.append(min(current_val, val))
        
    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

        
    def getMin(self) -> int:
        return self.min_stack[-1]
        
