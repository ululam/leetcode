class TrieNode:
    def __init__(self, letter, isWord = False):
        self.letter = letter
        self.child = {}
        self.isWord = isWord

    def add(self, word):
        if not word:
            return
        c = word[0]
        if c not in self.child:
            self.child[c] = TrieNode(c)
        self.child[c].isWord = self.child[c].isWord or len(word) == 1
        self.child[c].add(word[1:])

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # return self.wordBreakBFS(s, wordDict)
        # return self.wordBreakDpTopDown(s, wordDict)
        # return self.wordBreakDpBottomUp(s, wordDict)
        return self.wordBreakDpTrieOptimised(s, wordDict)

    def wordBreakDpTrieOptimised(self, s, wordDict):
        root = self._buildTrie(wordDict)
        n = len(s)
        dp = [False] * n
        for i in range(n):
            if i == 0 or dp[i-1]:
                curr = root
                for j in range(i, n):
                    c = s[j]
                    if c not in curr.child:
                        # No word exits
                        break
                    curr = curr.child[c]
                    if curr.isWord:
                        dp[j] = True

        return dp[n-1]
        
    def _buildTrie(self, wordDict) -> TrieNode:
        root = TrieNode(None)
        for word in wordDict:
            root.add(word)
        return root

    def wordBreakDpBottomUp(self, s, wordDict):
        n = len(s)
        dp = [False] * n
        for i in range(n):
            for word in wordDict:
                # Handle out of bound case (word is at the beginning and is bigger that current substr)
                start = i - len(word) + 1
                if start < 0:
                    continue
                # If word concludes the string (is prefix word) or there's solution at index i - len(word)
                if start == 0 or dp[i - len(word)]:
                    end = i + 1
                    # Check that substring is the word
                    if s[start:end] == word:
                        dp[i] = True
                        break
        return dp[n-1]
        


    def wordBreakDpTopDown(self, s, wordDict):
        memo = {}
        def dp(i):
            if i in memo:
                return memo[i]
            if i < 0:
                return True
            for word in wordDict:
                start = i - len(word) + 1
                end = i + 1
                if s[start:end] == word and dp(i - len(word)):
                    memo[i] = True
                    return True
            memo[i] = False
            return False
        
        return dp(len(s)-1)

    # O(n^3 + km), O(n + km)
    def wordBreakBFS(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        queue = deque([0])
        seen = set()
        n = len(s)
        while queue:
            start = queue.popleft()
            if start == n:
                return True
            for end in range(start+1, n+1):
                if end in seen:
                    continue
                if s[start:end] in words:
                    queue.append(end)
                    seen.add(end)
        return False

