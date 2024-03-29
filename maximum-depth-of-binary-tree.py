# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def count(root):
            if root is None:
                return 0
            if root.left is None:
                return count(root.right)+1
            if root.right is None:
                return count(root.left)+1
            return max(count(root.left),count(root.right))+1
        return count(root)
