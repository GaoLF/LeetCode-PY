# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} sum
    # @return {boolean}
    def hasPathSum(self, root, sum):
        if not root:
            return False
        res = 0
        if not root.left and not root.right:
            if sum == root.val:
                return True
            else:
                return False
        if root.left:
            res |= self.hasPathSum(root.left,sum-root.val)
        if root.right:
            res |= self.hasPathSum(root.right,sum-root.val)
        return bool(res)

    #def checkSum(self,root,sum,target):


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
#                      a(1)
#               b(2)           c(3)
#        d(4)       f(6)             e(5)
#                 g(7)
#               h(8)
print A.hasPathSum(a,5)
print A.hasPathSum(a,7)
print A.hasPathSum(a,9)
print A.hasPathSum(a,14)
print A.hasPathSum(a,24)
