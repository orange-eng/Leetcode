
# Leetcode practice
# author: orange
# date: 2021/6/1


# 栈的思想

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head:ListNode):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        p = head
        stack = []
        while p is not None:    
            stack.append(p.val)
            p = p.next
        
        #print("staCK=",(stack))
        output = ListNode(0)
        q = output
        for i in range(len(stack)-1,-1,-1):
            q.next = ListNode(stack[i])
            q = q.next
        output = output.next
        return output



# 定义链表的操作，一定要记住
list1 = ListNode()    #头指针一直没有改变，只是p一直在滑动，并定义了每一个结点的value
nums1 = [1]

p = list1
for i in range(len(nums1)):
    p.next = ListNode(nums1[i])
    p = p.next
list1 = list1.next

# -----------------------------------------------
example = Solution()
output = example.reverseList(list1)

p = output
while p is not None:
    print(p.val)
    p = p.next
    