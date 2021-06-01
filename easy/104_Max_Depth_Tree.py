
# Leetcode practice
# author: orange
# date: 2021/5/31

# 递归法。一般是
# if root is None:
#     return 0
# else:
#     return "递归算法"


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        num = 0
        if root is None:
            return 0
        else:
            return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))


l1 = TreeNode(1)
l2 = TreeNode(2)
l3 = TreeNode(3)
l4 = TreeNode(4)

root = l1
l1.left = l2
l1.right = l3

example = Solution()
output = example.maxDepth(root)
print(output)