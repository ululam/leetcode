class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # abcc -> abc
        # adade => ade
        # aaaaa => a
        # abc abc => abc 


        # init a hashmap `positions`
        # init len var maxLenSeen = 0
        # init idnex currentSubstringStart = 0
        # going through the string from the beginning
        # we check if char is alrady there
        # if not, add char -> pos
        # if yes:
        #   * maxLenSeen = max(maxLenSeen, (i - currentSubstringStart))
        #   * currentSubstringStart = positions.get(currChar)
        #   * positions.put(currChar, i)

        # return maxLenSeen

        if len(s) < 2:
            return len(s)

        poses = [-1] * 128
        currentSubstringStart = 0
        maxLenSeen = 0;
        # s = dvdf
        # 
        # currentSubstringStart = 0
        # d: i = 0, d -> 0              css = 0     ml = 0
        # v: i = 1, d -> 0, v -> 1      css = 0     ml = 0
        # d: i = 2, d -> 2, v -> 1      css = 1     ml = 2
        # f: i = 3, d -> 2, v -> 1,f->3   
        # end of cycle: ssl = 3 -> ml = 3
        for i in range(0, len(s)):                  
            charOrd = ord(s[i])
            prevPos = poses[charOrd]
            if prevPos >= currentSubstringStart:
                subStrLen = i - currentSubstringStart
                maxLenSeen = maxLenSeen if maxLenSeen > subStrLen else subStrLen
                currentSubstringStart = prevPos + 1
            poses[charOrd] = i

        subStrLen = len(s) - currentSubstringStart
        maxLenSeen = maxLenSeen if maxLenSeen > subStrLen else subStrLen

        return maxLenSeen
            

