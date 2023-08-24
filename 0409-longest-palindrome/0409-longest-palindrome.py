class Solution(object):
    # abccccdd
    
    def longestPalindrome(self, s):
        if len(s) == 1:
            return 1
        
        singleCharCounter = 0
        count = 0
        charCounts = {}
        for c in s:                         # a b c c c c d d
            cCount = charCounts.get(c, 0)   # b
            if cCount == 1:                 # 
                count += 1                  # 
                cCount = 0
                singleCharCounter -= 1
            else:
                cCount = 1
                singleCharCounter += 1
            charCounts[c] = cCount          # a -> 1, b -> 1, c -> 1
        count = 2 * count
        count += 1 if singleCharCounter > 0 else 0 
        return count
