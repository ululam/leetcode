class Solution(object):
    def characterReplacement(self, s, k):
        res = 0
        counts = {}
        l = 0
        maxCount = 0
        for r in range(len(s)):
            counts[s[r]] = 1 + counts.get(s[r], 0)
            maxCount = max(maxCount, counts[s[r]])
            if r - l + 1 - maxCount > k:
                counts[s[l]] -= 1
                l += 1

            res = r - l + 1
        return res
