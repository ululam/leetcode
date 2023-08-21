class Solution(object):
    def characterReplacemen2t(self, s, k):
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
            windowLen = r - l + 1
            if windowLen - maxCharCounter > k:
                # counters[ord(s[l])-shift] -= 1
                counters[s[l]] -= 1
                l += 1
            res = windowLen
        return res

    def characterReplacement(self, s, k):
        start = 0
        frequency_map = {}
        max_frequency = 0
        longest_substring_length = 0
        for end in range(len(s)):
            frequency_map[s[end]] = frequency_map.get(s[end], 0) + 1

            # the maximum frequency we have seen in any window yet
            max_frequency = max(max_frequency, frequency_map[s[end]])

            # move the start pointer towards right if the current
            # window is invalid
            is_valid = (end + 1 - start - max_frequency <= k)
            if not is_valid:
                frequency_map[s[start]] -= 1
                start += 1

            # the window is valid at this point, store length
            # size of the window never decreases
            longest_substring_length = end + 1 - start

        return longest_substring_length


