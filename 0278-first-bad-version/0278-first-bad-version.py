# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        # ----- | ----
        # 
        left, right, current = 0, n, 0
        while left <= right:
            current = left + ((right - left) >> 1)
            isBad = isBadVersion(current)
            if isBad:
                right = current - 1
            else:
                left = current + 1
        return left
