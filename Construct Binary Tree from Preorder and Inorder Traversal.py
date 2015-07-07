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
        return self.build(preorder,inorder,0,len(preorder)-1)

    def build(self,preorder,inorder,begin,end):
        #size = len(inorder)
        if begin > end:
            return None
        #if size == 1:
        #    return TreeNode(preorder[0])
        for i in range(begin,end+1):
            if inorder[i] == preorder[begin]:
                head = TreeNode(inorder[i])
                head.left = self.buildTree(preorder,inorder[begin:i])
                head.right = self.buildTree(preorder[i+1:end+1],inorder[i+1:end+1])
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
p(b)