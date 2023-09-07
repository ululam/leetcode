class Solution:
    def __init__(self):
        self.operations = {
            "+": lambda a,b: a + b,
            "-": lambda a,b: a - b,
            "*": lambda a,b: a * b,
            "/": lambda a,b: a / b
        }

    def evalRPN(self, tokens: List[str]) -> int:
        return self.evalInPlace(tokens)

    def evalInPlace(self, tokens: List[str]) -> int:
        # Go through list, apply operations in place, replacing (a,b,operations) triple with its result
        # Tranlate to nodes
        head = Node()
        node = head
        for t in tokens:
            node.val = t
            node.next = Node()
            node.next.prev = node
            node = node.next

        # Last node is odd
        node.prev.nxt = None

        node = head
        while node:
            print(f"{node.val} ->")
            node = node.next

        node = head
        while node:
            if node.val in self.operations.keys():
                x = int(node.prev.prev.val)
                y = int(node.prev.val)
                res = self.operations[node.val](x, y)
                currentNode = node.prev.prev
                currentNode.val = res
                currentNode.next = node.next
                if node.next:
                    node.next.prev = node.prev.prev 
            node = node.next

        return int(head.val)

    def evalViaStack(self, tokens: List[str]) -> int:
        # go through list
        # if number, add to stack
        # if operation, pop two previous numbers from stack, apply opertation, put to stack
        stack = []
        for t in tokens:
            if t not in self.operations.keys():
                stack.append(t)
                continue

            y = int(stack.pop())
            x = int(stack.pop())
            stack.append(self.operations[t](x, y))
        
        return int(stack.pop())

class Node:
    def __init__(self):
        self.val = ""
        self.prev = None
        self.next = None
