# Leetcode practice
# author: orange
# date: 2021/5/30


# 递归解法,值得学习

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True
        elif p is not None and q is not None:
            if p.val == q.val:
                return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
            else:
                return False
        else:
            return False


l1 = TreeNode(1)
l2 = TreeNode(2)
l2 = TreeNode(3)