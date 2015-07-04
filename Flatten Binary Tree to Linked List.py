# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {void} Do not return anything, modify root in-place instead.
    def flatten(self, root):
        nodes = []
        self.fill_List(root,nodes)
        temp = root
        for i in range(1,len(nodes)):
            temp.left = None
            temp.right = nodes[i]
            temp = temp.right

    def fill_List(self,root,nodes):
        if root:
            nodes.append(root)
            if root.left:
                self.fill_List(root.left,nodes)
            if root.right:
                self.fill_List(root.right,nodes)


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
A.flatten(d)
while d:
    print d.val
    d = d.right