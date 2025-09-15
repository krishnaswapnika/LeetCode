# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        q = deque([root])
        level = 0
        while q:
            size = len(q)
            prev = None
            for _ in range(size):
                node = q.popleft()
                if level % 2 == 0:
                    if node.val % 2 == 0:
                        return False
                    if prev is not None and node.val <= prev:
                        return False
                else:
                    if node.val % 2 == 1:
                        return False
                    if prev is not None and node.val >= prev:
                        return False
                prev = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return True
