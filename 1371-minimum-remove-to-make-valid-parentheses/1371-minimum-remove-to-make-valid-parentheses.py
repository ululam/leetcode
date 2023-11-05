class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            c = s[i]
            if c == ')':
                if stack and stack[-1][0] == '(':
                    stack.pop()
                else:
                    stack.append((c, i))
            if c == '(':
                stack.append((c, i))

        toRemove = set([p[1] for p in stack])
        res = []
        for i in range(len(s)):
            if i not in toRemove:
                res += s[i]
        return "".join(res)
