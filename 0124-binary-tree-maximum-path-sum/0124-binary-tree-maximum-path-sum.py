# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxs = float('-inf') 
        def dfs(node):
            if not node:
                return 0
            l = max(dfs(node.left), 0)
            r = max(dfs(node.right), 0)
            csum = node.val + l + r
            self.maxs = max(self.maxs, csum)
            return node.val + max(l, r)
        dfs(root)
        return self.maxs