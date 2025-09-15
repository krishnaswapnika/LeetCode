# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.sum = 0
        def revinorder(node):
            if not node:
                return
            revinorder(node.right)
            self.sum += node.val
            node.val = self.sum
            revinorder(node.left)
        revinorder(root)
        return root