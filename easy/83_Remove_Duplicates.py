# Leetcode practice
# author: orange
# date: 2021/5/30


# 使用指针的滑动思想
# 如果发现下一项相同，那么改变next即可
# 如果发现下一项不同，那么直接改变本身

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        else:
            q = head        # 移动指针
            while q.next is not None:
                if q.val == q.next.val:     # 如果发现下一项是一样的，那么跳过它（改变next即可）
                    q.next = q.next.next
                else:                       # 如果不一样，那么直接向前移动即可
                    q = q.next
            return head


list1 = ListNode()
p = list1
nums = [1,1,2,2,2,3,3,3,3,4]

for i in range(len(nums)):
    p.next = ListNode(nums[i])
    p = p.next

list1 = list1.next

# p = list1

# while p is not None:
#     print("list1:",p.val)
#     p = p.next

example = Solution()
output = example.deleteDuplicates(list1)

q = output
while q is not None:
    print("output:",q.val)
    q = q.next

