# Leetcode practice
# author: orange
# date: 2021/5/27



#在开头创建一个指针，这样就不妨碍头指针的判断

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head == None:
            return None
        my_head = ListNode(-1)  #在开头创建一个指针，这样就不妨碍头指针的判断
        my_head.next = head
        p = my_head

        while p.next is not None:
            if p.next.val == val:
                p.next = p.next.next
                #p = p.next
            else:
                p =p.next
        my_head = my_head.next
        return my_head



# 定义链表的操作，一定要记住
list1 = ListNode()    #头指针一直没有改变，只是p一直在滑动，并定义了每一个结点的value
list2 = ListNode()
nums1 = [1,2,2,2,2,2,2,4]
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
output = example.removeElements(list1,2)

p = output
while p is not None:
    print(p.val)
    p = p.next
    