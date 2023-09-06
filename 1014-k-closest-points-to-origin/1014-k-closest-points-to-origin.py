from collections import defaultdict

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Calculate all the distances
        # Put into array
        # sort
        # return first k
        # O(nlogn), n = len(points)
        if k == len(points):
            return points

        distances = defaultdict(list)
        for p in points:
            distances[p[0]*p[0] + p[1]*p[1]].append(p)    

        sorted_distances = sorted([k for k in distances.keys()])

        res = []
        # Get lists and join elememt
        for d in sorted_distances:
            points_list = distances[d]
            for p in points_list:
                res.append(p)
                if len(res) == k:
                    return res 
        