class Solution(object):
    def characterReplacement(self, s, k):
        # ABCBD, 2 - > 2 
        # ABCCCD, 1 -> 4 (CCCC)
 
        # counters = [0] * 26
        # shift = ord('A') # 65
        counters = {}
        res = 0
        maxCharCounter = 0
        l = 0
        for r in range(len(s)):
            #counters[ord(s[r])-shift] += 1 
            counters[s[r]] =  counters.get(s[r], 0) + 1
            maxCharCounter = max(maxCharCounter, counters[s[r]])
            if r - l + 1 - maxCharCounter > k:
                # counters[ord(s[l])-shift] -= 1
                counters[s[l]] -= 1
                l += 1
            res = r - l + 1
        return res

