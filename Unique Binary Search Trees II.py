#coding=utf-8
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# 把一个长的函数分成好几个小函数，真的能让步骤简单很多！
class Solution:
    # @param {integer} n
    # @return {TreeNode[]}
    def generateTrees(self, n):
        root = TreeNode(1)
        res = [root]
        if not n:
            return [None]
        if n == 1:
            return res
        i = 2
        while i <= n:
            temp = []
            for iter in res:
                self.built(iter,temp,i)
            res = temp
            i += 1
        return res

    def built(self,root,res,i):
        root_cp = TreeNode(i)
        root_cp.left = self.copy(root)
        res.append(root_cp)
        temp = root
        while temp:
            root_cp = self.copy(root)
            temp_cp = root_cp
            temp_nd = root

            while temp_nd != temp:
                temp_cp = temp_cp.right
                temp_nd = temp_nd.right
            #print temp.val,temp_nd.val
            temp_right = temp_cp.right
            newNode = TreeNode(i)
            temp_cp.right = newNode
            newNode.left = temp_right
            res.append(root_cp)

            temp = temp.right



    def copy(self,root):
        if root:
            root_new = TreeNode(root.val)
            if root.left:
                root_new.left = self.copy(root.left)
            if root.right:
                root_new.right = self.copy(root.right)
            return root_new
        else:
            return None

    def p(self,T):
        if T:
            print T.val
            if T.left:
                self.p(T.left)
            if T.right:
                self.p(T.right)

A = Solution()
"""
a = TreeNode(1)
b = TreeNode(2)
a.left = b
c = TreeNode(3)
c = A.copy(a)
A.p(c)
"""

res = A.generateTrees(4)
for i in res:
    A.p(i)
    print