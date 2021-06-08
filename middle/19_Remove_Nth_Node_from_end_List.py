# Leetcode practice
# author: orange
# date: 2021/6/8



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        slow = head
        fast = head
        if head.next == None:
            return None
        
        for i in range(n):
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        if n == 1:
            slow.next = None
        else:
            slow.next = slow.next.next
    
        return head

# 暴力解法
#Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
#         p = head
#         point_sum = 0
#         if p.next == None and n == 1:
#             return None

#         while p is not None:
#             point_sum += 1
#             p = p.next
#         #print(point_sum)
#         nth_point = point_sum - n
#         number = 0
#         q = head
#         if n != 1:
#             while number != nth_point:
#                 number += 1
#                 q = q.next

#             q.val = q.next.val
#             q.next = q.next.next
#         else:
#             while number != nth_point -1:
#                 number += 1
#                 q = q.next
#             q.next = None
#         return head

# 可以使用双指针
# 快慢指针，快指针先走n步，然后快慢一起走，
# 直到快指针走到最后，要注意的是可能是要删除第一个节点，
# 这个时候可以直接返回head -> next

        
# 定义链表的操作，一定要记住
list1 = ListNode()    #头指针一直没有改变，只是p一直在滑动，并定义了每一个结点的value

nums1 = [1,2]

p = list1
for i in range(len(nums1)):
    p.next = ListNode(nums1[i])
    p = p.next
list1 = list1.next


# -----------------------------------------------
example = Solution()
output = example.removeNthFromEnd(list1,1)

p = output
while p is not None:
    print(p.val)
    p = p.next