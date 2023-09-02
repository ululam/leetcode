# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        preLeft = left = right = head
        for i in range(0, n):
            right = right.next
            if not right:
                return head.next

        while right:
            preLeft = left
            left = left.next
            right = right.next

        preLeft.next = left.next

        return head
        