#coding=utf-8
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
#自己脑子里有屎，不要犯2B错误了，复制粘贴一定要仔细比对
class Solution:
    # @param {TreeNode} root
    # @param {integer} sum
    # @return {integer[][]}
    def pathSum(self, root, sum):
        res = []
        if not root:
            return []
        self.solve(root,0,res,[],sum)
        return res

    def solve(self,root,sum,res,vec,target):
        sum += root.val
        if not root.left and not root.right:
            if sum == target:
                vec.append(root.val)
                res.append(vec[:])
                del(vec[len(vec)-1])
            return
        if root.left:
            vec.append(root.val)
            self.solve(root.left,sum,res,vec,target)
            del(vec[len(vec)-1])
        if root.right:
            vec.append(root.val)
            self.solve(root.right,sum,res,vec,target)
            del(vec[len(vec)-1])


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
print A.pathSum(a,None)