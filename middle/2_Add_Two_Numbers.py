
# Leetcode practice
# author: orange
# date: 2021/5/31

# 注意指针为空的处理方式
# 核心代码
'''
if point1:
    x = point1.val
else:
    x = 0
if point2:
    y = point2.val
else:
    y = 0
s = x + y + carry
carry = s//10
point3.next = ListNode(s%10)
point3 = point3.next
'''



class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None and l2 == None:
            return None
        elif l1 == None and l2 is not None:
            return l2
        elif l1 is not None and l2 is None:
            return l1
        else:
            carry = 0
            point1 = l1
            point2 = l2
            l3 = ListNode()
            point3 = l3
            while point1 is not None or point2 is not None:
                if point1:
                    x = point1.val
                else:
                    x = 0
                if point2:
                    y = point2.val
                else:
                    y = 0
                s = x + y + carry
                carry = s//10
                point3.next = ListNode(s%10)
                point3 = point3.next

                if point1 != None: point1 = point1.next
                if point2 != None: point2 = point2.next
            if carry > 0:       # 当最后一次出现进位时
                point3.next = ListNode(1)
            l3 = l3.next
            return l3

# 定义链表的操作，一定要记住
list1 = ListNode()    #头指针一直没有改变，只是p一直在滑动，并定义了每一个结点的value
list2 = ListNode()
nums1 = [2,4,3]
nums2 = [5,6,4]

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

example = Solution()
output = example.addTwoNumbers(list1,list2)

p = output
while p is not None:
    print(p.val)
    p = p.next