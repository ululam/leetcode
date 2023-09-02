class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort intervals by start pos (should use end as a second sort param?)
        # Go through intervals taking ith and i+1th
        #   - If no intersection, continue
        #   - Otherwise merge using min, max
        if len(intervals) < 2:
            return intervals
        res = []
        sortedIntervals = self.sort(intervals)
        a1 = sortedIntervals[0]
        for i in range(1, len(sortedIntervals)):
            a2 = sortedIntervals[i]
            if a1[1] < a2[0]: 
                res += [a1]
                a1 = a2
            else:
                a1[0] = min(a1[0], a2[0])
                a1[1] = max(a1[1], a2[1])
        return res + [a1]
    
    
    def sort(this, intervals: List[List[int]]) -> List[List[int]]:
        return sorted(intervals, key=lambda l: l[0])