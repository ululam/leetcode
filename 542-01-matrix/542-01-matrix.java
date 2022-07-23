class Solution {
    public int[][] updateMatrix(int[][] mat) {
        for (int i=0;i<mat.length;i++) {
            for (int j=0;j<mat[i].length;j++) {
                if (mat[i][j] == 1) {
                    mat[i][j] = Integer.MAX_VALUE;
                }
            }
        }

        boolean allSet = false;
        int curr0 = -1;
        while (!allSet) {
            if (++curr0 > mat.length + mat[0].length) {
                break;
            };
            allSet = true;
            //System.out.printf("curr0 = %s\n", curr0);
            for (int i=0;i<mat.length;i++) {
                for (int j=0;j<mat[i].length;j++) {
                    if (mat[i][j] < Integer.MAX_VALUE) {
                        continue;
                    }
                    allSet = false;
                    if (i > 0 && mat[i-1][j] == curr0) {
                        mat[i][j] = Math.min(curr0 + 1, mat[i][j]);
                        //System.out.printf("Set [%s][%s] = %s\n", i,j, mat[i][j]);
                        continue;
                    }
                    if (i < mat.length-1  && mat[i+1][j] == curr0) {
                        mat[i][j] = Math.min(curr0 + 1, mat[i][j]);
                        //System.out.printf("Set [%s][%s] = %s\n", i,j, mat[i][j]);
                        continue;
                    }
                    if (j > 0  && mat[i][j-1] == curr0) {
                        mat[i][j] = Math.min(curr0 + 1, mat[i][j]);
                        //System.out.printf("Set [%s][%s] = %s\n", i,j, mat[i][j]);
                        continue;
                    }
                    if (j < mat[i].length - 1  && mat[i][j+1] == curr0) {
                        mat[i][j] = Math.min(curr0 + 1, mat[i][j]);
                        // System.out.printf("Set [%s][%s] = %s\n", i,j, mat[i][j]);
                        continue;
                    }
                }
            }
        }
        
        return mat;
    }
    
    private boolean setAndReturnIfChanged(int[][] mat, int i, int j, int val) {
        if (mat[i][j] > val) {
            mat[i][j] = val;
            return true;
        }
        
        return false;
    }
}