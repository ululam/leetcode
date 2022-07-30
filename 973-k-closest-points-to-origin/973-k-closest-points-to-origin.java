import java.util.Map.Entry;
//import java.util.stream.Stream;

class Solution {
    public int[][] kClosest(int[][] points, int k) {
        final Map<Integer, List<int[]>> dists = new TreeMap<>();
        for (int i=0; i< points.length; i++) {
            int dist = points[i][0]*points[i][0] + points[i][1]*points[i][1];
            List dList = Collections.singletonList(points[i]);
            dists.merge(dist, dList, (l1, l2) -> 
                        Stream.concat(l1.stream(), l2.stream())
                            .collect(Collectors.toList()));
        }
        
        
        return dists.entrySet().stream()
            .map(Entry::getValue)
            .flatMap(List::stream)
            .limit(k)
            .collect(Collectors.toList())
            .toArray(new int[k][2]);
        
    }
}