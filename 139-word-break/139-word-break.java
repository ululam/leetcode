class Solution {
    private int level = 0;
    
    public boolean wordBreak(String s, List<String> wordDict) {
        final Set<String> words = new HashSet<>(wordDict);
        final Queue<Integer> queue = new LinkedList<>();
        queue.add(0);
        
        boolean[] seen = new boolean[s.length()];
        
        while (!queue.isEmpty()) {
            int start = queue.poll();
            
            if (seen[start]) {
                continue;
            }
            
            for (int i = start+1; i<=s.length(); i++) {
                String sub = s.substring(start, i);
                if (words.contains(sub)) {
                    if (i == s.length()) {
                        return true;
                    }
                    queue.add(i);
                }
            }
            seen[start] = true;
        }
        
        return false;
    }
}