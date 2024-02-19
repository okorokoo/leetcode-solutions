# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ListNode.pos = 0
        while head:
            if head.pos:
                return True
            else:
                head.pos = 1
            head = head.next

        return False