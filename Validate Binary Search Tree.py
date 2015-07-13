# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isValidBST(self, root):
        turn = []
        self.trans(root,turn)

        for i in range(1,len(turn)):
            if turn[i-1] >= turn[i]:
                return False
        return True

    def trans(self,root,turn):
        if root:
            if root.left:
                self.trans(root.left,turn)
            turn.append(root.val)
            if root.right:
                self.trans(root.right,turn)

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
print A.isValidBST(c)