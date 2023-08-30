class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in intervals:
            if not newInterval or i[1] < newInterval[0]:
                res += [i]
            elif i[0] > newInterval[1]:
                res += [newInterval]
                newInterval = None
                res += [i]
            else:
                newInterval = [min(i[0], newInterval[0]), max(i[1], newInterval[1])]

        if newInterval:
            res += [newInterval]

        return res

