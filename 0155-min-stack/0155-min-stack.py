class MinStack:

    def __init__(self):
        self.head = None
        self.min = None

    def push(self, val: int) -> None:
        if not self.min:
            if not self.head:
                # If no min, start tracking only if stack was emptied
                self.min = val
        else:
            self.min = min(self.min, val)
        self.head = Node(val, self.head)
            
        # print(f"push({val}): {self.head}, min = {self.min}")

    def pop(self) -> None:
        if self.head:
            res = self.head.val
            if res == self.min:
                self.min = None
            self.head = self.head.next
            self.min = None
        else:
            res = None

        # print(f"pop: {self.head}, min = {self.min}")
        return res


    def top(self) -> int:
        print(f"top: {self.head}")
        return self.head.val if self.head else None

    def getMin(self) -> int:
        if not self.min and self.head:
            self.min = float('inf')
            node = self.head
            while node:
                self.min = min(self.min, node.val)
                node = node.next
        # print(f"getMin: min = {self.min}")
        return self.min if self.min < float('inf') else None
        
class Node:
    def __init__(self, val: int, next = None):
        self.val = val
        self.next = next
    
    def __str__(self):
        addon = f" -> {self.next}" if self.next else ""
        return f"[{self.val}]{addon}"


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()