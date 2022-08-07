class Solution {
    private static final int MIN_CODE = 32; // space
    private static final int SYMBOLS_NUMBER = 127 - 32;

    public int lengthOfLongestSubstring(String s) {
        // we start from the left end
        // Moving with two pointers: start and index
        // check if arr[char] > start:
        // we seen duplication =>
        // max_len = Math.max(max_len, index - start)
        // start = arr[char] (+1)
        // arr[char] = index
        // else:
        // store the chars we met in array: arr[char] = index
        
        // if reached the end, return Math.max(max_len, index-start)
        
        final char[] chars = s.toCharArray();
        if (chars.length < 2) {
            return chars.length;
        }
        
        int max_len = 0;
        int start = 0;
        int i;
        Integer[] seenChars = new Integer[SYMBOLS_NUMBER];
        for (i=0; i< chars.length; i++) {
            final int c_idx = chars[i] - MIN_CODE;
            if (seenChars[c_idx] != null && seenChars[c_idx] >= start) {
                max_len = Math.max(max_len, i - start);
                start = seenChars[c_idx] + 1;
                p("> '%s', max_len = %s, len = %s, start = %s, i = %s", chars[i], max_len, i - start, start, i);
            } else {
                p("'%s', max_len = %s, len = %s, start = %s, i = %s", chars[i], max_len, i - start, start, i);
            }
            // TODO For 0 pos, here lies a problem
            seenChars[c_idx] = i;
        }
        
        if (start == -1)
            return chars.length;
        
        return Math.max(max_len, chars.length - start);
    }
    
    void p(String s, Object... args) {
        System.out.printf(s + "\n", args);
    }
}