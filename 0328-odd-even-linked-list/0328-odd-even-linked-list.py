# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next:
            return head

        odd = head
        even = head.next

        firstEven = even


        # 1 -> 2 -> 3 -> 4 -> 5
        # ^.   ^
        # a) 1 -> 3 -> 4 -> 5 & 2 -> 3 -> ...
        #    ^                  ^
        # b) 1 -> 3 -> 4 -> 5 & 2 -> 3 -> 4 ...
        #         ^             ^
        # c) 1 -> 3 -> 4 -> 5 & 2 -> 4 -> 5 -> ...
        #         ^             ^
        # d) 1 -> 3 -> 4 -> 5 -> null & 2 -> 4 -> 5 -> null
        #         ^                  ^
        # a1) 1 -> 3 -> 4 -> 5 -> null & 2 -> 4 -> 5 -> null
        #         ^                  ^
        # b1) 1 -> 3 ->  5 -> null & 2 -> 4 -> 5 -> null
        #         ^                  ^
        # c1) 1 -> 3 ->  5 -> null & 2 -> 4 -> 5 -> null
        #                ^                ^
        # d1) 1 -> 3 ->  5 -> null & 2 -> 4 ->  null
        #                ^                ^
        while even and even.next:
            lastOdd = odd
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = firstEven

        return head