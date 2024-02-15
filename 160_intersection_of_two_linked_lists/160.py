# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, A: ListNode, B: ListNode) -> Optional[ListNode]:
        a = A
        b = B
        if A == None and B == None:
            return None
        while a != b:
            if a == None:
                a = B
            else:
                a = a.next
            if b == None:
                b = A
            else:
                b = b.next
        return a