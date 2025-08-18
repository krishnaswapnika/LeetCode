# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        def lheight(node):
            h=0
            while node:
                h+=1
                node = node.left
            return h
        def rheight(node):
            h=0
            while node:
                h+=1
                node = node.right
            return h
        l= lheight(root.left)
        r= rheight(root.right)
        if lheight == rheight:
            return (1<< lheight) -1
        else:
            return 1+ self.countNodes(root.left) + self.countNodes(root.right)
