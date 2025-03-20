# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def rev_list(node):
            prev, cur = None, node
            while cur:
                cur.next, prev, cur = prev, cur, cur.next
            return prev
        
        dummy = ListNode()
        dummy.next = head
        prev = dummy

        while head:
            count = 0
            cur = head
            while count < k and cur:
                cur = cur.next
                count += 1
            if count == k:
                group = head
                for _ in range(k-1):
                    group = group.next
                next_group = group.next
                group.next = None
                new_group = rev_list(head)

                prev.next = new_group
                head.next = next_group

                prev = head
                head = next_group
            else:
                break
        return dummy.next
        