class Solution:
    def __init__(self):
        self.visited = None
        self.verified = None

    # 

    def exist(self, board: List[List[str]], word: str) -> bool:
        for n in range(len(board)):
            for k in range (len(board[n])):
                self.visited = set()
                if self._exist(board, word, n, k):
                    return True
        return False
    
    def _exist(self, board, word, v, h) -> bool:
        # print(f"Checking {word} at ({v},{h})")
        visitedKey = self._position_key(v, h) 
        if visitedKey in self.visited:
            return False
        if board[v][h] != word[0]:
            return False
        if len(word) < 2:
            return True
        
        self.visited.add(visitedKey)
        # Go up
        res = False
        if v > 0 and self._exist(board, word[1:], v-1, h):
            res = True
        # Go down
        elif v < len(board)-1 and self._exist(board, word[1:], v+1, h):
            res = True
        # Go left
        elif h > 0 and self._exist(board, word[1:], v, h-1):
            res = True
        # Go right
        elif h < len(board[v])-1 and self._exist(board, word[1:], v, h+1):
            res = True 
        
        self.visited.remove(visitedKey)

        return res


    def _remove_cell_and_return(self, x, y, res) -> bool:
        key = self._position_key(x, y)
        if key in self.visited:
            self.visited.remove(key)
        return res


    def _key(self, word, x, y):
        return f"{word}_{x}_{y}"
    
    def _position_key(self, x, y):
        return self._key("", x, y)