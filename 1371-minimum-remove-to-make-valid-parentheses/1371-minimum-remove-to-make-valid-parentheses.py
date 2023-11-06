class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # return self.minRemoveToMakeValidStack(s)
        return self.minRemoveToMakeValidStackless(s)

    def minRemoveToMakeValidStackless(self, s: str) -> str:
        unmatchedOpenCounter, totalOpenCounter = 0, 0
        removeIndexes = set()
        for i in range(len(s)):
            c = s[i]
            if c == ')':
                if unmatchedOpenCounter == 0:
                    removeIndexes.add(i)
                else:
                    unmatchedOpenCounter -= 1
            elif c == '(':
                unmatchedOpenCounter += 1
                totalOpenCounter += 1

        leaveOpenCount = totalOpenCounter - unmatchedOpenCounter
        res = []
        for i in range(len(s)):
            if i in removeIndexes:
                continue
            c = s[i]
            if c == '(':
                if leaveOpenCount > 0:
                    res.append(c)
                    leaveOpenCount -= 1
            else:
                res.append(c)
        return "".join(res)


    def minRemoveToMakeValidStack(self, s: str) -> str:
        stack = []
        res = list(s)
        for i in range(len(s)):
            c = s[i]
            if c == ')':
                if stack:
                    stack.pop()
                else:
                    res[i] = ""
            if c == '(':
                stack.append(i)

        for i in stack:
            res[i] = ""
        
        return "".join(res)
