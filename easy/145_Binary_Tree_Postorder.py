
# Leetcode practice
# author: orange
# date: 2021/5/31




class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 迭代法
# class Solution(object):
#     def preorderTraversal(self, root):
#         """
#         :type root: TreeNode
#         :rtype: List[int]
#         """
#         if not root:
#             return []
        
#         stack = [root]
#         res = []
#         while stack:
#             cur = stack.pop()
#             res.append(cur.val)            
#             if cur.right:
#                 stack.append(cur.right)     # 栈结构，先放右边的，再放左边的
#             if cur.left:
#                 stack.append(cur.left)
#         return res

# 递归法：
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        else:
            return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) +[root.val]