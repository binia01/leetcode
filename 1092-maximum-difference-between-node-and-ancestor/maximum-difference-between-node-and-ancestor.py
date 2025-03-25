# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node, mi, ma):
            
            if not node:
                return 0
            nonlocal ans

            res = max(abs(mi - node.val), abs(ma - node.val))
            ans = max(ans, res)

            nmi = min(mi, node.val)
            nmx = max(ma, node.val)

            dfs(node.left, nmi, nmx)
            dfs(node.right, nmi, nmx)
            return ans
        return dfs(root, root.val, root.val)