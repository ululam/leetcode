class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        int[] ramsom = new int[26];
        int totalUniqueChars = 0;
        for (char c : ransomNote.toCharArray()) {
            int index = c - 'a';
            if (ramsom[index]++ == 0) {
                totalUniqueChars++;
            }
        }
        
        for (char c : magazine.toCharArray()) {
            int index = c - 'a';
            if (--ramsom[index] == 0) {
                if (--totalUniqueChars == 0) {
                    return true;
                };
            }
        }
        
        return false;
    }
}