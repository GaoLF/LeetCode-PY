# Definition for a binary tree node.
#coding=utf-8
import sys
# 我利用的方法就是：中序遍历就是二叉查找树的顺序
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} k
    # @return {integer}
    def kthSmallest(self, root, k):
        if not root:
            return 0
        return self.findkth(root,k,0)[0];

    def findkth(self,root,k,i):
        #print root.val,k,i
        if not root:
            return [sys.maxint,i]
        left_res = [sys.maxint,i]
        if root.left:
            left_res = self.findkth(root.left,k,i)
        if left_res[0] != sys.maxint:
            return left_res
        if left_res[1]+1 >= k:
            return [root.val,0]
        right_res = [sys.maxint,left_res[1]+1]
        if root.right:
            right_res = self.findkth(root.right,k,left_res[1]+1)
        return right_res

A = Solution()
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
b.left = a
b.right = c
c.right = d
d.right = e

print A.kthSmallest(None,3)
print A.kthSmallest(b,1)
print A.kthSmallest(b,2)
print A.kthSmallest(b,3)
print A.kthSmallest(b,4)
print A.kthSmallest(b,5)
