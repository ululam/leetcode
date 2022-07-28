class Solution {
    public int[][] updateMatrix(int[][] mat) {
        int rows = mat.length;
        int cols = mat[0].length;
        int dists[][] = new int[rows][cols];

        for (int i=0; i< rows; i++) {
            for (int j=0; j< cols; j++) { 
                dists[i][j] = Integer.MAX_VALUE - 10000;
            }
        }

        
        for (int i=0; i< rows; i++) {
            for (int j=0; j< cols; j++) { 
                if (mat[i][j] == 0) {
                    dists[i][j] = 0;
                } else {
                    if (i > 0) {
                        dists[i][j] = Math.min(dists[i][j], dists[i-1][j] + 1);
                    }
                    
                    if (j > 0) {
                        dists[i][j] = Math.min(dists[i][j], dists[i][j-1] + 1);
                    }
                }
            }
        }

        for (int i=rows-1; i>=0 ; i--) {
            for (int j=cols-1; j>=0; j--) { 
                if (mat[i][j] != 0) {
                    if (i < rows-1) {
                        dists[i][j] = Math.min(dists[i][j], dists[i+1][j] + 1);
                    }
                    
                    if (j < cols - 1) {
                        dists[i][j] = Math.min(dists[i][j], dists[i][j+1] + 1);
                    }
                }
            }
        }
        
        return dists;
    }
   
//     public int[][] updateMatrix(int[][] mat) {
//         final int rows = mat.length;
//         if (rows == 0) {
//             return mat;
//         }
//         final int cols = mat[0].length;
        
//         final int[][] dists = new int[rows][cols];
//         final Queue<Tuple> queue = new LinkedList<>();
//         for (int i=0; i< rows; i++) {
//             for (int j=0; j<cols; j++) {
//                 dists[i][j] = Integer.MAX_VALUE;
//                 if (mat[i][j] == 0) {
//                     dists[i][j] = 0;
//                     queue.add(new Tuple(i,j));
//                 }
//             }
//         }
//         int moves[][] = new int[][] {
//             {-1, 0}, {1, 0}, {0, -1}, {0, 1}
//         };
        
//         while (!queue.isEmpty()) {
//             Tuple t = queue.poll();
//             for (int i=0; i<4; i++) {
//                 int row = t.row + moves[i][0];
//                 int col = t.col + moves[i][1];
//                 if (row >= 0 && col >= 0 && row < rows && col < cols) {
//                     if (dists[row][col] > dists[t.row][t.col] + 1) {
//                         dists[row][col] = dists[t.row][t.col] + 1;
//                         queue.add(new Tuple(row, col));
//                     }
//                 }
//             }
//         }
        
//         return dists;
//     }
    
//     private class Tuple {
//         final int row;
//         final int col;
//         Tuple(int row, int col) {
//             this.row = row;
//             this.col = col;
//         }
//     }
}