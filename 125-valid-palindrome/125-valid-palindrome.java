class Solution {
    public boolean isPalindrome(String s) {
        final char[] chars = s.toCharArray();
        int j = chars.length;
        for (int i=0; i < chars.length; i++) {
            char ci = chars[i];
            if (!isAlphaN(ci)) {
                continue;
            }
            
            char cj = 0;
            for (j=j-1;j>=0;j--) {
                if (isAlphaN(chars[j])) {
                    break;
                }
            }
            
            
            if (! eq(ci, chars[j]) ) {
                return false;
            }
            
            if (j <= i) {
                break;
            }
        }
        
        return true;
    }
    
    private boolean isAlphaN(char c) {
        return (c >= 48 && c <= 57) || (c >= 97 && c <= 122)
            || (c >= 65 && c <= 90);
    }
    
    private boolean eq(char c1, char c2) {
        return c1 == c2 || (c1 > 57 && c2 > 57 && (c1 - 32 == c2 || c1 + 32 == c2));
    }
}