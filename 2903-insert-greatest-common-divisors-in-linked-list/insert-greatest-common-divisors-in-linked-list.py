# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        cur = head.next

        while cur:
            gcd_node = ListNode(math.gcd(prev.val, cur.val))
            prev.next = gcd_node
            gcd_node.next = cur
            prev = cur
            cur = cur.next
        return head
        