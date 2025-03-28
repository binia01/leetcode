# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []

        def dfs(node, level):
            if not node:
                return
            if level == len(res):
                res.append(node.val)
            else:
                res[level] = max(res[level], node.val)

            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

            return res

        return dfs(root, 0)



          

        