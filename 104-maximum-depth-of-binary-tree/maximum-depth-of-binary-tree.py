# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        count = 0
        if not root:
            return count
        count +=1
        lcount = rcount = 0
        lcount = self.maxDepth(root.left)
        rcount = self.maxDepth(root.right)
        count += max(lcount, rcount)

        return count
        