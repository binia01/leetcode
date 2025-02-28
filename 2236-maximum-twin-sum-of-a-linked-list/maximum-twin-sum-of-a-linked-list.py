# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        vals = []
        cur = head
        while cur:
            vals.append(cur.val)
            cur = cur.next

        max_sum = 0
        n = len(vals)
        for i in range(n):
            max_sum = max(vals[i] + vals[n-1-i], max_sum)
        return max_sum