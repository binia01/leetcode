# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        ans = []
        def dfs(node, level):
            if not node:
                return

            if level == len(ans):
                ans.append([])

            if level % 2 == 0:
                ans[level].append(node.val)
            else:
                ans[level].insert(0, node.val)
                
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
            return ans
        return dfs(root, 0)


        