class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        # interate over magavine, construct hasmap c -> count
        # interate over ransomNote, decrease count in the hashmap for given char
        # if count < 0, return False
        # if we reached the end of the ransom note, return True

        # rn = abcc, magagine = abcabc
        letterCounts = [0] * 26
        shift = ord('a')
        for c in magazine:
            cIndex = ord(c) - shift
            letterCounts[cIndex] += 1
        for c in ransomNote:   
            cIndex = ord(c) - shift                         # a
            letterCounts[cIndex] -=1
            if letterCounts[cIndex] < 0:                               # false
                return False
        return True


        # Complexity: O(len(rn) + len(m))
        # Memory: O(26)

