# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.detectCycleHash2p(head)

    def detectCycleHash(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = set()
        while head:
            if head in visited:
                return head
            visited.add(head)
            head = head.next

        return None

    def detectCycleHash2p(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        t,h = head, head
        
        met = False
        while h and h.next:
            t = t.next
            h = h.next.next
            if t == h:
                met = True
                break
        
        if not met:
            return None
        
        h = head
        while t != h:
            t = t.next
            h = h.next
        return h

        