class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        # interate over magavine, construct hasmap c -> count
        # interate over ransomNote, decrease count in the hashmap for given char
        # if count < 0, return False
        # if we reached the end of the ransom note, return True

        # rn = abcc, magagine = abcabc
        letterCounts = {}
        for c in magazine:
            letterCounts[c] = 1 + letterCounts.get(c, 0) # a -> 2, b -> 2, c -> 2
        for c in ransomNote:                            # a
            count = letterCounts.get(c, 0) - 1          # 0
            if count < 0:                               # false
                return False
            letterCounts[c] = count                     # 0
        return True


        # Complexity: O(len(rn) + len(m))
        # Memory: O(26)

