class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for n in range(len(board)):
            for k in range (len(board[n])):
                if self._exist(board, word, n, k):
                    return True
        return False
    
    def _exist(self, board, word, v, h) -> bool:
        # print(f"Checking {word} at ({v},{h})")
        if board[v][h] != word[0]:
            return False
        if len(word) < 2:
            return True
        
        board[v][h] = '#'
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
        
        board[v][h] = word[0]

        return res

