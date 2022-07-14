class Solution {
    private static final int MAX_VALUE = 6;

    public int minDominoRotations(int[] A, int[] B) {
        int[] aCounts = new int[MAX_VALUE];
        int[] bCounts = new int[MAX_VALUE];
        int[] dupleCounts = new int[MAX_VALUE];
        
        for (int i = 0; i < A.length; i++) {
            aCounts[A[i]-1]++;
            bCounts[B[i]-1]++;
            if (A[i] == B[i]) {
                dupleCounts[A[i]-1]++;
            }
        }

//         System.out.println("A ----------");
//         for (int i = 0; i < aCounts.length; i++) {
//             System.out.println(aCounts[i]);
//         }
        
//         System.out.println("B ----------");
        
//         for (int i = 0; i < bCounts.length; i++) {
//             System.out.println(bCounts[i]);
//         }

//         System.out.println("DUPLE ----------");
       
//         for (int i = 0; i < dupleCounts.length; i++) {
//             System.out.println(dupleCounts[i]);
//         }

        
        int minRotations = A.length;
        for (int i = 0; i < MAX_VALUE; i++) {
            if (aCounts[i] + bCounts[i] - dupleCounts[i] == A.length) {
                int minRotations2 = Math.min(aCounts[i], bCounts[i]) - dupleCounts[i];
                minRotations = Math.min(minRotations, minRotations2);
            }           
        }
        
        return minRotations == A.length ? -1 : minRotations;
    }
}