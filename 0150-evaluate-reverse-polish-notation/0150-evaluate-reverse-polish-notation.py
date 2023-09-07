class Solution:
    def __init__(self):
        self.operations = {
            "+": lambda a,b: a + b,
            "-": lambda a,b: a - b,
            "*": lambda a,b: a * b,
            "/": lambda a,b: a / b
        }
    def evalRPN(self, tokens: List[str]) -> int:
        return self.evalViaStack(tokens)

    def evalInPlace(self, tokens: List[str]) -> int:
        # Go through list, apply operations in place, replacing (a,b,operations) triple with its result
        pass

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
