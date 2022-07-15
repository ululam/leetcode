/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        sum(new ListNode(0, l1), new ListNode(0, l2), false);
        return l1;
    }
    
    private void sum(ListNode l1, ListNode l2, boolean plusOne) {
        if (l1.next == null) {
            if (l2.next == null) {
                if (plusOne) {
                    l1.next = new ListNode(1);
                }
                return;
            }
            
            l1.next = l2.next;
            finalize1(l1, plusOne);
            return;
            
        }

        if (l2.next == null) {
            finalize1(l1, plusOne);
            return;
        }

        l1.next.val += l2.next.val + (plusOne ? 1 : 0);
        plusOne = l1.next.val > 9;
        
        if (plusOne) {
            l1.next.val -= 10; 
        }

        sum(l1.next, l2.next, plusOne);
    }
 
    private void finalize1(ListNode l, boolean plusOne) {
        if (!plusOne) {
            return;
        }
        
        if (l.next == null) {
            l.next = new ListNode(1);
            return;
        }
        
        if (l.next.val < 9) {
            l.next.val++;
            return;
        }
            
        l.next.val = 0;
        finalize1(l.next, true);
    }
    
}