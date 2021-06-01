# Leetcode practice
# author: orange
# date: 2021/6/1



# 有点难，递归法没有看懂



class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 方法1 递归法
# class Solution:
#     def invertTree(self, root):
#         if not root:
#             return
#         root.left, root.right = self.invertTree(root.right),self.invertTree(root.left)
#         return root


# 方法2 栈方法
class Solution:
    def invertTree(self, root):
        res,stack = [],[root]
        if not root:return root
        while stack:
            temp = [ ]
            for node in stack:
                if node:
                    node.left,node.right = node.right,node.left
                    temp.append(node.left)
                    temp.append(node.right)
            stack = temp
        return root
