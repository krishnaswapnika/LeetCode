# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.prev = None
        self.diff = float("inf")
        def dfs(node):
            if not node:
                return 
            dfs(node.left)
            if self.prev is not None:
                self.diff = min(self.diff, node.val-self.prev)
            self.prev = node.val 
            dfs(node.right)
        dfs(root)
        return self.diff