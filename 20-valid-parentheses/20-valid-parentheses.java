class Solution {
    public boolean isValid(String s) {
        if (s.length() % 2 != 0) {
            return false;
        }
        final Stack<Character> stack = new Stack<>();
        for (char c : s.toCharArray()) {
            if (c == '}' || c == ')' || c == ']') {
                if (stack.isEmpty()) {
                    return false;
                }
                Character el = stack.pop();
                if (c == '}' && el != '{') {
                    return false;
                }
                if (c == ')' && el != '(') {
                    return false;
                }
                if (c == ']' && el != '[') {
                    return false;
                }
                
                continue;
            }
            
            stack.push(c);
        }
        
        return stack.isEmpty();
    }
}