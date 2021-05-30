
# Leetcode practice
# author: orange
# date: 2021/5/30


# 典型的二叉树+栈方法

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                res.append(root.val)
                root = root.right
        return res 

# class Solution(object):
#     def inorderTraversal(self, root):
#         """
#         :type root: TreeNode
#         :rtype: List[int]
#         """
#         res = []
#         self.iterative_inorder(root,res)
#         return res

#     def iterative_inorder(self,root,res):
#         stack = []
#         while root or stack:
#             if root:
#                 stack.append(root)
#                 root = root.left
#             else:
#                 root = stack.pop()
#                 res.append(root.val)
#                 root = root.right
#         return res

l1 = TreeNode(1)
l2 = TreeNode(2)
l3 = TreeNode(3)
l4 = TreeNode(4)

root = l1
l1.left = l2
l1.right = l3

example = Solution()
output = example.inorderTraversal(root)
print(output)