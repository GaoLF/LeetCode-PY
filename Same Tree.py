# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {boolean}
    
    #python中True和False：除了''、""、0、()、[]、{}、None为False之外，其他的都是True
    #这个地方写return 1 0居然不对
    def isSameTree(self, p, q):
        if p and q:
            if p.val == q.val:
                return (self.isSameTree(p.left,q.left) & self.isSameTree(p.right,q.right))
            else:
                return False
        elif p == None and q == None:
            return True
        else:
            return False