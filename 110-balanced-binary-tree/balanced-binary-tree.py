# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if not node:
                return 0

            lcount = height(node.left)
            rcount = height(node.right)
            
            if lcount == -1 or rcount == -1 or abs(lcount - rcount) > 1:
                return -1
            
            return 1 + max(lcount, rcount)
        return height(root) != -1
        
        