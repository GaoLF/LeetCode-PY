#coding=utf-8
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    # 自己琢磨了半天也没做出来，其实是那么简单，不断往下遍历，当节点的值在p和q的之间，则当前节点就是他们的最小祖先
    # 为了进一步节省计算，如果当前节点小于p和q，往当前节点的右节点走，当前节点的值大于p和q的值，则当前节点往左子树遍历
    def lowestCommonAncestor(self, root, p, q):
        while (root.val - p.val) * (root.val - q.val) > 0:
            root = (root.left, root.right)[p.val > root.val]
        return root
    """我根本就没做出来！
    def lowestCommonAncestor(self, root, p, q):
        res = [root]
        self.inorder(root,[0,0],res,p,q)
        return res[0]


    def inorder(self,root,pq,head,p,q):
        if root:
            temp = head[0]
            if pq == [1,1]:
                return
            if root.left:
                if pq == [0,0]:
                    head[0] = root.left
                self.inorder(root.left,pq,head,p,q)

            if root.right:
                if pq == [0,0]:
                    head[0] = root.right
                self.inorder(root.right,pq,head,p,q)
            if root == p or root == q:
                if pq == [0,0]:
                    if root == p:
                        pq = [1,0]
                    else:
                        pr = [0,1]
                else:
                    pq = [1,1]
                    return
            head[0] = temp
            """

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
print A.lowestCommonAncestor(a,g,h).val