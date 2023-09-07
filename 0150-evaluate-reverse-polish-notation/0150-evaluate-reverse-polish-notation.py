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
        pos = 0
        while len(tokens) > 1:
            if tokens[pos] not in self.operations.keys():
                pos += 1
                continue
            x = int(tokens[pos-2])
            y = int(tokens[pos-1])
            res = self.operations[t](x, y)
            tokens[pos] = res
            token.pop(pos)
            token.pop(pos)
            pos -=1

        return int(tokens[0])

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
