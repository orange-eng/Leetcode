
# Leetcode practice
# author: orange
# date: 2021/5/31



# 写出结束条件
# 不要把树复杂化，就当做树是三个节点，根节点，左子节点，右子节点
# 只考虑当前做什么，不用考虑下次应该做什么
# 每次调用应该返回什么
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
    
        return self.get_hight(root)

    def get_hight(self,root):
        if root is None:
            return 0
        if root.left is None and root.right is not None:    # NULL结点不参与比较过程
            return 1 + self.get_hight(root.right)
        if root.left is not None and root.right is None:
            return 1+ self.get_hight(root.left)
        
        left = self.get_hight(root.left)
        right = self.get_hight(root.right)
        return 1 + min(left,right)

