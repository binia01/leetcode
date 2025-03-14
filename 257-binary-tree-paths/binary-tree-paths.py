# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        res = []
        def dfs(node):
            if node is None:
                return 
            res.append(str(node.val))
            if node.left is None and node.right is None:
                ans.append("->".join(res))
            else:
                dfs(node.left)
                dfs(node.right)
            res.pop()
        dfs(root)
        return ans
        
        