# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        nodes = list()
        n = head
        while n:
            nodes.append(n)
            n = n.next
        pos = len(nodes) >> 1 

        return nodes[pos]
