from collections import defaultdict

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Calculate all the distances
        # Put into array
        # sort
        # return first k
        # O(nlogn), n = len(points)
        # if k == len(points):
        #     return points

        return sorted(points, key = lambda p: p[0]**2 + p[1]**2)[:k]
        # D = [] #heap for storing tuple (distance, point)
        # for pt in points:
        #     x, y = pt[0], pt[1]
        #     d = x * x + y * y
        #     heapq.heappush(D, (-d, pt))
        #     if len(D) > k:
        #         heapq.heappop(D)
        # return [pt for (d, pt) in D]        