#coding=utf-8
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#****************************************************************
#****************************************************************
#第一次提交又没对，只需改一个小小的地方即可，改之前只满足所有数都为正数的情况
#*********返回的时候，如果是负数就返回0，就能确保把负数的影响取消掉！******
#****************************************************************
#****************************************************************
class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def maxPathSum(self, root):
        res = [-1<<30]
        if not root:
            return 0
        self.pathSum(root,res)
        return res[0]
    def pathSum(self,root,res):
        #print res
        if not root:
            return 0
        left,right = 0,0
        if root.left:
            left = self.pathSum(root.left,res)
        if root.right:
            right = self.pathSum(root.right,res)
        if root.val + left + right > res[0]:
            res[0] = root.val + left + right
        return max(0,max(left,right) + root.val)# 就是这一行，第一遍做的时候没有给他加上与0的对比！！
        #这一点需要注意



A = Solution()
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(2)
d = TreeNode(4)
e = TreeNode(-1)
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
print A.maxPathSum(c)