# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def sumNumbers(self, root):
        return self.sumof_Tree(root,0)

    def sumof_Tree(self,root,up_v):
        if not root:
            return up_v
        sum = up_v*10 + root.val
        res = 0
        if root.left:
            res += self.sumof_Tree(root.left,sum)
        if root.right:
            res += self.sumof_Tree(root.right,sum)
        if not root.left and not root.right:
            res += sum
        return res

A = Solution()
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
g = TreeNode(7)
h = TreeNode(8)
a.left = b
a.right = c
b.left = d
c.right = e
b.right = f
f.left = g
g.left = h
print A.sumNumbers(a)
