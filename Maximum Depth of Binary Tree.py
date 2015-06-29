# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def maxDepth(self, root):
        res = self.nextDepth(root,0)
        return res

    def nextDepth(self, root, depth):
        if root == None:
            return  depth
        if root.left and root.right:
            return max(self.nextDepth(root.left,depth+1),self.nextDepth(root.right,depth+1))
        elif root.left:
            return self.nextDepth(root.left,depth+1)
        elif root.right:
            return self.nextDepth(root.right,depth+1)
        else:
            return depth+1