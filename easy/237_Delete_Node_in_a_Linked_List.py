# Leetcode practice
# author: orange
# date: 2021/6/1



# 把下一个结点复制一下，然后再跳过下一个结点


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        p = node
        p = p.next
        node.val = p.val
        node.next = node.next.next

