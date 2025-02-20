# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # cur = head
        # prev = None

        # while cur:
        #     temp = cur.next
        #     cur.next = prev
        #     prev = cur
        #     cur = temp
        # print(prev)
        # print(d)
        # while prev and head:
        #     if prev.val != head.val:
        #         return False
        #     prev = prev.next
        #     head = head.next
        # return True
        stk = []
        cur = head
        while cur:
            stk.append(cur.val)
            cur = cur.next

        while head:
            c = stk.pop()
            if head.val != c:
                return False
            head = head.next
        return True
