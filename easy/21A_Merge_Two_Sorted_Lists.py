# Leetcode practice
# author: orange
# date: 2021/5/27

# 不太明白。程序在leetcode上面可以运行，但是在本地跑不了

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 == None:
            return l2
        if l2 == None:
            return l1

        preHead = ListNode(-1)
        p1 = l1
        p2 = l2
        cur = preHead

        while p1 != None and p2 != None:
            if p1.val < p2.val:
                cur.next = p1
                cur = p1
                p1 = p1.next

            else:
                cur.next = p2
                cur = p2
                p2 = p2.next

        if p1:
            cur.next = p1

        if p2:
            cur.next = p2

        return preHead.next

# class Solution(object):
#     def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         res = ListNode(None)
#         node = res
#         while l1 and l2:
#             if l1.val < l2.val:
#                 node.next,l1 = l1,l1.next
#             else:
#                 node.next,l2 = l2,l2.next
#             if l1:
#                 node.next = l1
#             if l2:
#                 node.next = l2
#         return res.next


example = Solution()
l1 = [1,2,3,4]
l2 = [1,3,4,10,11]
output = example.mergeTwoLists(l1,l2)
print(output)