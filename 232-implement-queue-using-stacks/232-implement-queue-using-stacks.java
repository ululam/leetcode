class MyQueue {
    
    private final Stack<Integer> direct = new Stack<>();
    private final Stack<Integer> queue = new Stack<>();
    
    private int topX;
    
    public MyQueue() {
        
    }
    
    public void push(int x) {
        if (direct.isEmpty()) {
            topX = x;
        }
        direct.push(x);
    }
    
    public int pop() {
        if (queue.isEmpty()) {
            while (!direct.isEmpty()) {
                queue.push(direct.pop());
            }

        }
        
        return queue.pop();
    }
    
    public int peek() {
        if (!queue.isEmpty()) {
            return queue.peek();
        }
        return topX;
    }
    
    public boolean empty() {
        return queue.isEmpty() && direct.isEmpty();
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */