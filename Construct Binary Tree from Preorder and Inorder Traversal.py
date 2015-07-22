# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param {integer[]} preorder
    # @param {integer[]} inorder
    # @return {TreeNode}
    def buildTree(self, preorder, inorder):
        return self.build(preorder,inorder,0,len(preorder)-1,0,len(inorder))

    def build(self,preorder,inorder,pb,pe,ib,ie):
        #size = len(inorder)
        if pb > pe:
            return None
        #if size == 1:
        #    return TreeNode(preorder[0])
        for i in range(0,ie-ib+1):
            if inorder[i+ib] == preorder[pb]:
                head = TreeNode(inorder[i+ib])
                head.left = self.build(preorder,inorder,pb+1,pb+i,ib,ib+i-1)
                head.right = self.build(preorder,inorder,pb+i+1,pe,ib+i+1,ie)
                return head


A = Solution()
b = A.buildTree([],[])
a = A.buildTree([1,2,4,5,3,6,7],[4,2,5,1,6,3,7])
def p(a):
    if a:
        print a.val
        if a.left:
            p(a.left)
        if a.right:
            p(a.right)
#p(a)
p(a)