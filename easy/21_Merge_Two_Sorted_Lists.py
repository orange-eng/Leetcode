# Leetcode practice
# author: orange
# date: 2021/5/27


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1, l2):
        p = l1
        q = l2
        output = ListNode()
        output_Node = output
        while p is not None and q is not None:
            if p.val >= q.val:
                output_Node.next = q
                q = q.next
                output_Node = output_Node.next
            else:
                output_Node.next = p
                p = p.next
                output_Node = output_Node.next
        if p is None:
            output_Node.next = q
        elif q is None:
            output_Node.next = p
        output = output.next
        return output


# 定义链表的操作，一定要记住
list1 = ListNode()    #头指针一直没有改变，只是p一直在滑动，并定义了每一个结点的value
list2 = ListNode()
nums1 = [1,2,4]
nums2 = [1,3,4]

p = list1
for i in range(len(nums1)):
    p.next = ListNode(nums1[i])
    p = p.next
list1 = list1.next

q = list2
for i in range(len(nums2)):
    q.next = ListNode(nums2[i])
    q = q.next
list2 = list2.next

# -----------------------------------------------
example = Solution()
output = example.mergeTwoLists(list1,list2)

p = output
while p is not None:
    print(p.val)
    p = p.next
    