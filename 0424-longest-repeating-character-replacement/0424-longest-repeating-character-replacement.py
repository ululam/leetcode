class Solution(object):
    def characterReplacement(self, s, k):
        # ABCBD, 2 - > 2 
        # ABCCCD, 1 -> 4 (CCCC)
 
        # counters = [0] * 26
        # shift = ord('A') # 65
        counters = {}
        res = 0
        l = 0
        for r in range(len(s)):
            #counters[ord(s[r])-shift] += 1 
            counters[s[r]] = 1 + counters.get(s[r], 0)
            windowLen = r - l + 1
            if windowLen - max(counters.values()) > k:
                # counters[ord(s[l])-shift] -= 1
                counters[s[l]] -= 1
                l += 1
            else:
                res = max(res, windowLen)
        return res


