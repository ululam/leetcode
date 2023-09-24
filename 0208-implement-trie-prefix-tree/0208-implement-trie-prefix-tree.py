class Trie:

    def __init__(self):
        self.head = Node(-2)
        self.TERMINAL = Node(-1)

    def insert(self, word: str) -> None:
        prev = self.head
        for c in word:
            node = prev.next.get(c)
            if not node:
                node = Node(c)
                prev.next[c] = node
            prev = node
        prev.terminal = True


    def search(self, word: str) -> bool:
        node = self.head
        for c in word:
            node = node.next.get(c)
            if node is None:
                break
        return node is not None and node.terminal

    def startsWith(self, prefix: str) -> bool:
        node = self.head
        for c in prefix:
            node = node.next.get(c)
            if node is None:
                break
        return node is not None


class Node:
    def __init__(self, letter):
        self.letter = letter
        self.next = {}
        self.terminal = False

    def addNext(self, n):
        self.next[n.letter] = n

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)