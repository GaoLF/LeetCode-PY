# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

# ������ȻҲ�ύ������ųɹ�
# ���뵽res��int�����п���Ϊ�գ�����Ϊ�յ�ʱ���ȻҲ�����ȥ�ˣ�
# ���о���rootΪNoneʱӦ�÷���[]������Ӧ����None�����������ֺö���ˣ�
class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        stack = [root]
        res = [[root.val]]
        i = 0
        while stack:
            temp = []
            ints = []
            for iter in stack:
                if iter.left:
                    temp.append(iter.left)
                    ints.append(iter.left.val)
                if iter.right:
                    temp.append(iter.right)
                    ints.append(iter.right.val)
            if ints:
                if i%2:
                    res.append(ints)
                else:
                    res.append(ints[::-1])
            stack = temp
            i += 1
        return res

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
print A.zigzagLevelOrder(a)