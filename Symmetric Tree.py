#Definition for a binary tree node.
#coding=utf-8
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    # 空的时候，返回True，真是把你妈杀了，不能给个提示么，哥哥的ac率啊！！！
    def isSymmetric(self, root):
        if not root:
            return True
        stack = [root]
        while stack:
            temp = []
            for iter in stack:
                if iter:
                    temp.append(iter.left)
                    temp.append(iter.right)
            nums = []
            for iter in temp:
                if iter:
                    nums.append(iter.val)
                else:
                    nums.append('#')
            if nums != nums[::-1]:
                return False
            stack = temp
        return True


A = Solution()
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(2)
d = TreeNode(3)
e = TreeNode(3)
f = TreeNode(4)
a.left = b
a.right = c
b.left = d
c.right = e
b.right = f
print A.isSymmetric(a)
print A.isSymmetric(b)