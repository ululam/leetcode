class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # go through list
        # if number, add to stack
        # if operation, pop two previous numbers from stack, apply opertation, put to stack
        stack = []
        operations = ["/", "*", "+", "-"]
        for t in tokens:
            if t not in operations:
                stack.append(t)
                continue
            y = int(stack.pop())
            x = int(stack.pop())
            if t == "+":
                stack.append(x + y)
            elif t == "-":
                stack.append(x - y)
            elif t == "*":
                stack.append(x * y)
            elif t == "/":
                stack.append(x / y)
        
        return int(stack.pop())
