class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        final int initialColor = image[sr][sc];
        if (initialColor == color) {
            return image;
        }
        
        image[sr][sc] = color;
        
        if (sr > 0 && image[sr-1][sc] == initialColor) {
            floodFill(image, sr-1, sc, color);
        }
        if (sr < image.length-1 && image[sr+1][sc] == initialColor) {
            floodFill(image, sr+1, sc, color);
        }
        if (sc > 0 && image[sr][sc-1] == initialColor) {
             floodFill(image, sr, sc-1, color);
        }
        if (sc < image[sr].length-1 && image[sr][sc+1] == initialColor) {
             floodFill(image, sr, sc+1, color);
        }
        return image;
    }
}