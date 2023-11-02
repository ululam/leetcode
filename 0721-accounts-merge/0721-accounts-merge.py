class DSU:
    def __init__(self, length):
        self.repr = [i for i in range(0, length)]
        self.size = [1] * length

    def find(self, x):
        if x == self.repr[x]:
            return x
        # Path compression
        self.repr[x] = self.find(self.repr[x])
        return self.repr[x]

    def union(self, a, b):
        reprA = self.find(a)
        reprB = self.find(b)
        if reprA == reprB:
            return
        # Union by size: smaller joins to larger group
        if self.size[reprA] >= self.size[reprB]:
            self.size[reprA] += self.size[reprB]
            self.repr[reprB] = reprA
        else:
            self.size[reprB] += self.size[reprA]
            self.repr[reprA] = reprB
        

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # return self.accountsMergeGraph(accounts)
        return self.accountsMergeDSU(accounts)

    def accountsMergeDSU(self, accounts: List[List[str]]) -> List[List[str]]:
        # Disjoint Set Union aka Union-Find
        dsu = DSU(len(accounts))
        emailGroup = {}
        for i in range(len(accounts)):
            name = accounts[i][0]
            for email in accounts[i][1:]:
                if email in emailGroup:
                    dsu.union(i, emailGroup[email])
                else:
                    emailGroup[email] = i
        
        # Store email in repr groups
        components = {}
        for email, group in emailGroup.items():
            groupRep = dsu.find(group)
            if groupRep not in components:
                components[groupRep] = []
            components[groupRep].append(email)

        # Sort and add name
        res = []
        for group, component in components.items():
            sortedComp = [accounts[group][0]] + sorted(component)
            res.append(sortedComp)
        
        return res
# -------------------------

    def accountsMergeGraph(self, accounts: List[List[str]]) -> List[List[str]]:
        visited = set()
        adjMap = {}
        
        def addEmail(fromEmail, toEmail):
            if not fromEmail in adjMap:
                adjMap[fromEmail] = []
            adjMap[fromEmail].append(toEmail)

        def DFS(array, accEmail):
            visited.add(accEmail)
            array.append(accEmail)
            if not accEmail in adjMap:
                return
            for neib in adjMap[accEmail]:
                if not neib in visited:
                    DFS(array, neib)

        for a in accounts:
            for j in range(2, len(a)):
                addEmail(a[j], a[1])
                addEmail(a[1], a[j])
        
        mergedAccs = []
        for a in accounts:
            email1 = a[1]
            if email1 not in visited:
                mergedA = []
                DFS(mergedA, email1)
                mergedA = [a[0]] + sorted(mergedA)
                mergedAccs.append(mergedA)
        
        return mergedAccs

        
