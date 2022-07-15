class Solution {
    public String restoreString(String s, int[] indices) {
        if (s == null || s ==" ") {
            return s;
        }
        
        char[] chars = new char[indices.length];
        for (int i = 0; i < indices.length; i++) {
            chars[indices[i]] = s.charAt(i);
        }
        
        return new String(chars);
    }
}