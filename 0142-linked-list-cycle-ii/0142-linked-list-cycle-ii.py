# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.detectCycleHash(head)

    def detectCycleHash(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        visited = set()
        visited.add(head)
        while head.next:
            head = head.next
            if head in visited:
                return head
            visited.add(head)

        return None

    def detectCycleHash2p(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pass
        