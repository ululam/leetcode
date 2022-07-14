class LRUCache {

    private class LRUNode {
        private LRUNode prev;
        private LRUNode next;

        private int key;
        private int value;
        
        public String toString() {
            return "[" + key + ", " + value + "]";
        }
    }
    
    private final Map<Integer, LRUNode> cache;
    private final int capacity;
    private int size;
    private LRUNode head, tail;
    
    public LRUCache(int capacity) {
        this.cache = new HashMap<>(capacity);
        this.capacity = capacity;
        this.head = new LRUNode();
        this.tail = new LRUNode();
        this.head.next = tail;
        this.tail.prev = head;
    }
    
    public int get(int key) {
        LRUNode node = cache.get(key);
        if (node == null) 
            return -1;
        
        removeNode(node);
        moveToTail(node);
        
        return node.value;
    }
    
    public void put(int key, int value) {
        LRUNode node = cache.get(key);
        if (node == null) {
            node = new LRUNode();
            node.key = key;
            node.value = value;
            cache.put(key, node);
            moveToTail(node);
            
            if (++size > capacity) {
                // System.out.println("Ran out of capacity");
                // System.out.println("Removing node: " + this.head.next);
                cache.remove(this.head.next.key);
                removeNode(this.head.next);
                size--;   
            }
        } else {
            node.value = value;
            removeNode(node);
            moveToTail(node);
        }
    }
    
    private void moveToTail(LRUNode node) {
        //System.out.println("Moving to tail: " + node);
        //System.out.println("BEFORE: ");
        //showLL();
        LRUNode prevNode = tail.prev;
        prevNode.next = node;
        node.prev = prevNode;
        node.next = tail;
        tail.prev = node;

        //showLL();
    }
    
    private void removeNode(LRUNode node) {
        node.prev.next = node.next;    
        node.next.prev = node.prev;
    }
        
    private void showLL() {
        LRUNode node = this.head;
        while (node != null) {
            System.out.printf("%s -> ", node);
            node = node.next;
        }
        System.out.println("END");
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */