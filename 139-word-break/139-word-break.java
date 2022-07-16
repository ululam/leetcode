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
        
        return consists(s, parts);
    }
    
    private boolean consists(String s, Set<String> parts) {
        //p("%s'%s' ~ %s", t(), s, parts);
        if (s.length() == 0) {
            return true;
        }
        for (String w : parts) {
            if (!s.contains(w)) {
                continue;
            }
            String s1 = s.replaceAll(w, " ");
            if (s1.trim().length() == 0) {
                return true;
            }
            
            Set<String> narrowParts = new HashSet<>(parts);
            narrowParts.remove(w);
            
            level++;
            boolean allFound = true;
            for (String s2 : s1.split(" ")) {
                allFound = consists(s2, narrowParts); 
                if (!allFound) {
                    break;
                }
            }
            if (allFound) {
                return true;
            }
            level--;
        }
        
        return false;
    }
    
    private void p(String s, Object... params) {
        System.out.printf(s + "\n", params);
    }
    
    private String t() {
        StringBuffer res = new StringBuffer();
        for (int i=0; i<level;i++) {
            res.append("  ");
        }
        
        return res.toString();
    }
}