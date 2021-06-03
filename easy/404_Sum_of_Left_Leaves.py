

# Leetcode practice
# author: orange
# date: 2021/6/3



# 递归法

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root:TreeNode):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:        # 终止条件
            return 0
        if root.left and root.left.left == None and root.left.right == None:    # 一旦发现左节点
            return root.left.val + self.sumOfLeftLeaves(root.right)
        else:
            return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right) # 否则继续
