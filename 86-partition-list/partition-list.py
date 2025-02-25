# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        a = ListNode()
        b = ListNode()

        p = a
        q = b

        cur = head
        while cur:
            if cur.val < x:
                p.next = cur
                p = p.next
            else:
                q.next = cur
                q = q.next
            cur = cur.next

        q.next = None
        p.next = b.next

        return a.next

        