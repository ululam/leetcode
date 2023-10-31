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

        for a in accounts:
            for j in range(2, len(a)):
                addEmail(a[1], a[j])
                addEmail(a[j], a[1])
        
        mergedAccs = []
        for a in accounts:
            email1 = a[1]
            if email1 not in visited:
                mergedA = []
                DFS(mergedA, email1)
                mergedA = [a[0]] + sorted(mergedA)
                mergedAccs.append(mergedA)
        
        return mergedAccs

        
