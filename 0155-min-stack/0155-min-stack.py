class MinStack:

    def __init__(self):
        self.head = None

    def push(self, val: int) -> None:
        self.head = Node(val, self.head)

    def pop(self) -> None:
        val, self.head = (self.head.val, self.head.next) if self.head else (None, None)
        return val

    def top(self) -> int:
        return self.head.val if self.head else None

    def getMin(self) -> int:
        return self.head.min if self.head else None
        
class Node:
    def __init__(self, val: int, next = None):
        self.val = val
        self.next = next
        self.min = min(self.val, next.min) if next else self.val

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()