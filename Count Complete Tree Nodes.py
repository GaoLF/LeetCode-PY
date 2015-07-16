#coding=utf-8
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# 唉，即便是第二次做，还是第一时间想不出简便方法
# 为什么是统计完全二叉树的节点个数，因为有很多节点的子树是满满的
# 通过判断一个节点是否满，如果满，直接返回结果，不满返回左右和，像正常一样

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def countNodes(self, root):
        i = j = 0
        if not root:
            return 0
        temp = root
        while temp:
            i += 1
            temp = temp.left
        temp = root
        while temp:
            j += 1
            temp = temp.right
        if i == j:
            return 2**i - 1
        return self.countNodes(root.left) + self.countNodes(root.right) + 1


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
print A.countNodes(a)