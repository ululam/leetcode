class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # return self.minRemoveToMakeValidStack(s)
        return self.minRemoveToMakeValidStackless(s)

    def minRemoveToMakeValidStackless(self, s: str) -> str:
        l = list(s)
        unmatchedOpenCounter, totalOpenCounter = 0, 0
        for i, c in enumerate(l):
            if c == ')':
                if unmatchedOpenCounter == 0:
                    l[i] = '*'
                else:
                    unmatchedOpenCounter -= 1
            elif c == '(':
                unmatchedOpenCounter += 1
                totalOpenCounter += 1

        leaveOpenCount = totalOpenCounter - unmatchedOpenCounter
        res = []
        for c in l:
            if c == '*':
                continue
            if c == '(':
                if leaveOpenCount > 0:
                    res.append(c)
                    leaveOpenCount -= 1
            else:
                res.append(c)
        return "".join(res)


    def minRemoveToMakeValidStack(self, s: str) -> str:
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
