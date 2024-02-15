# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        H = ListNode(0, head)
        cur = H
        while cur:
            try:
                if cur.next.val == val:
                    cur.next = cur.next.next
                else:
                    cur = cur.next
            except:
                break
        return H.next