class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left, right = [], []
        for i in intervals:
            if i[1] < newInterval[0]:
                left += [i]
            elif i[0] > newInterval[1]:
                right += [i]
            else:
                newInterval = [min(i[0], newInterval[0]), max(i[1], newInterval[1])]

        return left + [newInterval] + right

