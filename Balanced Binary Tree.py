# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isBalanced(self, root):
        return self.check_Tree(root)[0]

    def check_Tree(self,root):
        res = [True,0]
        if not root:
            return res
        #if root.left:
        left = self.check_Tree(root.left)
        right = self.check_Tree(root.right)
        if not left[0]&right[0]:
            return [False,0]
        res[1] = max(left[1],right[1])+1
        if abs(left[1]-right[1])>1:
            res[0] = False
        return res

A = Solution()
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)

a.left = b
#a.right = c
b.left = d
print A.isBalanced(a)



