#coding=utf-8
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    # 这个题我想要不要每次只取右节点，没有右节点取左节点，实际是不行的，因为如果左边比右边深度深
    # 然后即便右边有，但还要转到左边
    # 所以还是老老实实的用堆栈吧
    def rightSideView(self, root):
        vec = []
        res = []
        if root:
            vec.append(root)
        while vec:
            temp = []
            for iter in vec:
                if iter.left:
                    temp.append(iter.left)
                if iter.right:
                    temp.append(iter.right)
            res.append(vec[len(vec)-1].val)
            vec = temp
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
#                      a(1)
#               b(2)           c(3)
#        d(4)       f(6)             e(5)
#                 g(7)
#               h(8)
print A.rightSideView(None)