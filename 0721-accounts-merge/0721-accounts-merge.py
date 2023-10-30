class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        visited = set()
        adjMap = {}
        
        def addEmail(theEmail, toEmail):
            if not toEmail in adjMap:
                adjMap[toEmail] = []
            adjMap[toEmail].append(theEmail)

        def DFS(acc, accEmail):
            visited.add(accEmail)
            acc.append(accEmail)
            if not accEmail in adjMap:
                return
            for neib in adjMap[accEmail]:
                if not neib in visited:
                    DFS(acc, neib)


        n = len(accounts)
        for a in accounts:
            aSize = len(a)
            email1 = a[1]
            for j in range(2, aSize):
                email = a[j]
                addEmail(email, email1)
                addEmail(email1, email)
        
        mergedAccs = []
        for a in accounts:
            email1 = a[1]
            if email1 not in visited:
                mergedA = [a[0]]
                DFS(mergedA, email1)
                mergedA = [mergedA[0]] + sorted(mergedA[1:])
                mergedAccs.append(mergedA)
        
        return mergedAccs

        
