# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {ListNode} head
    # @return {TreeNode}
    def sortedListToBST(self, head):
        return self.generate([head],self.count(head))

    def count(self,head):
        size = 0
        while head:
            head = head.next
            size += 1
        return size

    def generate(self,head,size):
        if not size:
            return None
        node = TreeNode(0)
        node.left = self.generate(head,size/2)
        node.val = head[0].val
        head[0] = head[0].next
        node.right = self.generate(head,size - size/2 - 1)
        return node


A = Solution()
a,b,c,d = ListNode(1),ListNode(2),ListNode(3),ListNode(4)
a.next = b
b.next = c
c.next = d
x = A.sortedListToBST(a)
def p(x):
    if x:
        print x.val
        if x.left:
            p(x.left)
        if x.right:
            p(x.right)
p(x)
"""
  ListNode *list;
    int count(ListNode *node){
        int size = 0;
        while (node) {
            ++size;
            node = node->next;
        }
        return size;
    }

    TreeNode *generate(int n){
        if (n == 0)
            return NULL;
        TreeNode *node = new TreeNode(0);
        node->left = generate(n / 2);
        node->val = list->val;
        list = list->next;
        node->right = generate(n - n / 2 - 1);
        return node;
    }

    TreeNode *sortedListToBST(ListNode *head) {
        this->list = head;
        return generate(count(head));
    }
    """