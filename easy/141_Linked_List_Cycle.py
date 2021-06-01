

# Leetcode practice
# author: orange
# date: 2021/5/31


# 方法3：考虑快慢指针法即可破题

# 方法1&2：过一个毁一个即可。这种方法太骚了

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# 方法1 
# class Solution(object):
    # def hasCycle(self, head):
    #     """
    #     :type head: ListNode
    #     :rtype: bool
    #     """
    #     while head:
    #         if head.val == 'bjfuvth':
    #             return True
    #         else:
    #             head.val = 'bjfuvth'
    #         head = head.next
    #     return False

# 方法2
# class Solution(object):
#     def hasCycle(self, head):
#         if not head:
#             return False
#         while head.next and head.val != None:
#             head.val = None  # 遍历的过程中将值置空
#             head = head.next
#         if not head.next:  # 如果碰到空发现已经结束，则无环
#             return False
#         return True  # 否则有环

# 方法3 快慢指针法
# 经典
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False




