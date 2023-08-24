# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        # 0 -> 1 -> 2
        # *    *    *
        # 0 <- [1    2 -> 3] -> 4

        # current = head

        # N-1, N -> N+1
        
        # current = head
        # nextNode = head.next

        # while nextNode:
        # nextNextNode = nextNode.next. (2)
        # nextNode.next = current       (1->0)
        # current = nextNode            (1)
        # nextNode = nextNextNode       (2)
        if not head or not head.next:
            return head
        # [1,2,3,4,5]
        first = head  # 1
        second = head.next
        head.next = None
        while second:
            third = second.next    # 5
            second.next = first         # 4 -> 3 -> 2 -> 1
            first = second              # 4
            second = third         # 5
        return first



