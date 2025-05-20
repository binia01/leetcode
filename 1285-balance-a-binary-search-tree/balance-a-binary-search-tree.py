# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def func(node):
            if node is None:
                return []
            
            left = func(node.left)
            right = func(node.right)

            return left + [node.val] + right

        res = func(root)

        def solve(res):
            if not res:
                return
            
            mid = len(res) // 2

            root = TreeNode(res[mid])
            root.left = solve(res[:mid])
            root.right = solve(res[mid+1:])
            return root
        return solve(res)
