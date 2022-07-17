class Solution {
    private int level = 0;
    
    public boolean wordBreak(String s, List<String> wordDict) {
        // Gor through list, select all words that are in the string
        // Add those words to set
        // For each word:
        // - (a) Remoev all occuremies. Remove word itself from set
        // - If leftover len == 0 => true
        // - If no, go to (a), with "contains" check.
        // - If all words are interated, false
        
        Set<String> parts = new HashSet<>();
        for (String w : wordDict) {
            if (s.contains(w)) {
                parts.add(w);
            }
        }
        
        return consists(s, parts, 0, new Boolean[s.length()]);
    }
    
    private boolean consists(String s, Set<String> parts, int start, Boolean[] seen) {
        if (start == s.length()) {
            return true;
        }
        
        if (seen[start] != null) {
            return seen[start];
        }
        
        for (int i=start+1;i<=s.length(); i++) {
            String prefix = s.substring(start, i);
            if (parts.contains(prefix) && consists(s, parts, i, seen)) {
                return seen[start] = true;
            }
        }
        
        return seen[start] = false;
    }
}