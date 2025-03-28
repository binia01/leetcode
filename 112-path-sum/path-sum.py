# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, cursum):
            if node is None:
                return False
            cursum += node.val
            if node.left is None and node.right is None and cursum == targetSum:
                return True
            return dfs(node.left, cursum) or dfs(node.right, cursum)
        return dfs(root, 0)

                
            
        