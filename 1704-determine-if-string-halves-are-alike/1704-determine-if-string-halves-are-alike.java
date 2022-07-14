class Solution {
    private static final Set<Character> VOWELS = new HashSet<>();

    static {
        VOWELS.add('a');
        VOWELS.add('e');
        VOWELS.add('i');
        VOWELS.add('o');
        VOWELS.add('u');
        VOWELS.add('A');
        VOWELS.add('E');
        VOWELS.add('I');
        VOWELS.add('O');
        VOWELS.add('U');
    }

    public boolean halvesAreAlike(String s) {
        final char[] sChars = s.toCharArray();
        final int halfSize = sChars.length >> 1;
        int count1 = 0;
        int count2 = 0;
        for (int i = 0; i < halfSize; i++) {
            count1 += isVowel(sChars[i]) ? 1 : 0;
            count2 += isVowel(sChars[i+halfSize]) ? 1 : 0;
        }
        
        return count1 == count2;
    }
    
    private boolean isVowel(char c) {
        return VOWELS.contains(c);
    }
    
}