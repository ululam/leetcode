class Solution(object):
    def checkInclusion(self, s1, s2):
        # 1. Build a hashmap c -> count on top of s1
        # 2. Using sliding window of size len(s1), move along s2
        # 3.   a. on start, go once through the window char by char, and decrease counters
        # = Store tuples: c -> (current, initial) and use intial to reset
        # - If faced a char which is not of s2, and move window to the char after the current
        # To avoid cycles over hashmap, add counter = len(s1), and decrease it each time
        # we faced a proper char
        # On reset, reset it back to the len(s1)
        # when its 0, return true
        # if reached the end, return false
        winSize = len(s1)
        s1Chars = {}
        for c in s1:
            cCount = s1Chars.get(c, [0, 0])
            cCount[0] += 1
            cCount[1] += 1
            s1Chars[c] = cCount
        
        left, right = 0, winSize
        s2Size = len(s2)
        s1CharCount = winSize

        while right <= s2Size:
            # If breaking char, reset
            shouldReset = False
            for ind in range(left, right):
                if s2[ind] in s1Chars:
                    v = s1Chars[s2[ind]]
                    v[0] -= 1

                    if v[0] < 0:
                        self._resetMap(s1Chars)
                        s1CharCount = winSize
                        left += 1
                        right = left + winSize
                        break
                    else:
                        s1CharCount -= 1
                        if s1CharCount == 0:
                            return True
                else:
                    # Breaking char
                    self._resetMap(s1Chars)
                    s1CharCount = winSize
                    left = ind+1
                    right = left + winSize
                    break

                    
            # If non-breaking, 
        return False

    def _resetMap(self, map):
        for k, v in map.iteritems():
            v[0] = v[1]    