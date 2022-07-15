class Solution {
    public int longestPalindrome(String s) {
        int[] letters = new int[58];
        int counter = 0;
        for (char c : s.toCharArray()) {
            int index = c - 'A';
            if (letters[index] == 1) {
                letters[index] = 0;
                counter += 2;
            } else {
               letters[index]++; 
            }
        }
        
        return counter < s.length() ? counter + 1 : counter;
    }
}