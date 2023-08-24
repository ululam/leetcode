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
        # head.next = None

        # while nextNode:
        # nextNextNode = nextNode.next. (2)
        # nextNode.next = current       (1->0)
        # current = nextNode            (1)
        # nextNode = nextNextNode       (2)
        # [1,2,3,4,5]
        prev = None
        current = head  # 1
        while current:
            nextNode = current.next    # 5
            current.next = prev         # 4 -> 3 -> 2 -> 1
            prev = current              # 4
            current = nextNode         # 5
        return prev



