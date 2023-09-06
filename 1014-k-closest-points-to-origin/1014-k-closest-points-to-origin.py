import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Calculate all the distances
        # Put into array
        # sort
        # return first k
        # O(nlogn), n = len(points)
        # if k == len(points):
        #     return points

        #return sorted(points, key = lambda p: p[0]**2 + p[1]**2)[:k]
        heap = []
        for (x, y) in points:
            dist = -(x*x + y*y)
            if len(heap) == k:
                heapq.heappushpop(heap, (dist, x, y))
            else:
                heapq.heappush(heap, (dist, x, y))
        
        return [(x,y) for (dist,x, y) in heap]
        # D = [] #heap for storing tuple (distance, point)
        # for pt in points:
        #     x, y = pt[0], pt[1]
        #     d = x * x + y * y
        #     heapq.heappush(D, (-d, pt))
        #     if len(D) > k:
        #         heapq.heappop(D)
        # return [pt for (d, pt) in D]        