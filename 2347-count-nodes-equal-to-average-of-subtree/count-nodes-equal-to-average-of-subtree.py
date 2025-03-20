# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        
        def dfs(node):
            if not node:
                return 0, 0

            
            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)

            ttl = left_sum + right_sum + node.val
            count = left_count + right_count + 1

            if ttl // count == node.val:
                nonlocal total
                total += 1

            return ttl, count
        
        total = 0
        dfs(root)

        return total


        