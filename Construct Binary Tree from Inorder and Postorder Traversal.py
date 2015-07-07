# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param {integer[]} inorder
    # @param {integer[]} postorder
    # @return {TreeNode}
    def buildTree(self, inorder, postorder):
        size = len(inorder)
        if not size or size != len(postorder):
            return None
        if size == 1:
            return TreeNode(postorder[0])
        for i in range(size):
            if inorder[i] == postorder[0]:
                head = TreeNode(inorder[i])
                head.left = self.buildTree(inorder[0:i],postorder[1:i+1])
                head.right = self.buildTree(inorder[i+1:size],postorder[i+1:size])
                return head

A = Solution()
a = A.buildTree([4,2,5,1,6,3,7],[1,2,4,5,3,6,7])
def p(a):
    if a:
        print a.val
        if a.left:
            p(a.left)
        if a.right:
            p(a.right)
p(a)