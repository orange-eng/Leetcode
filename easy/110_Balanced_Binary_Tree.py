
# Leetcode practice
# author: orange
# date: 2021/5/31

# 递归法。定义一个获得树高度的函数，并不断调用。
# 如果返回值为-1说明树已经不平衡

'''
模版一共三步，就是递归的三部曲：
找终止条件：什么时候递归到头了？此题自然是root为空的时候，空树当然是平衡的。
思考返回值，每一级递归应该向上返回什么信息？参考我代码中的注释。
单步操作应该怎么写？因为递归就是大量的调用自身的重复操作，因此从宏观上考虑，只用想想单步怎么写就行了，
左树和右树应该看成一个整体，即此时树一共三个节点：root，root.left，root.right。
'''



class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def max_depth(root):
            if root is None:
                return 0
            left = max_depth(root.left)
            if(left == -1):
                return -1       # 一旦出现不平衡，马上返回-1
            right = max_depth(root.right)
            if(right == -1):
                return -1       # 一旦出现不平衡，马上返回-1
            if abs(left - right)>1:
                return -1       # 一旦出现不平衡，马上返回-1
            else:
                return 1 + max(left,right)

        return max_depth(root) != -1
# class Solution:
#     def get_Height(self, root):
#         """
#         定义函数语义： 返回以root为根节点的二叉树的高度
#         """

#         if root == None:   # 递归终止条件
#             return 0

#         left_h = self.get_Height(root.left)
#         right_h = self.get_Height(root.right)

#         if abs(left_h - right_h) > 1:
#             self.flag = False

#         return max(right_h, left_h) + 1
 

#     def isBalanced(self, root):
#         self.flag = True
#         self.get_Height(root)
#         return self.flag

l1 = TreeNode(1)
l2 = TreeNode(2)
l3 = TreeNode(3)
l4 = TreeNode(4)
l5 = TreeNode(5)

root = l1
l1.left = l2
l1.right = l3
l2.right = l4
l4.right = l5
example = Solution()
output = example.isBalanced(root)
print(output)