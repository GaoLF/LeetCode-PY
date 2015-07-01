#Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def inorderTraversal(self, root):
        res = []
        if root is None:
            return res
        if root.left:
            res = res + self.inorderTraversal(root.left)
        res.append(root.val)
        if root.right:
            res = res + self.inorderTraversal(root.right)
        return res