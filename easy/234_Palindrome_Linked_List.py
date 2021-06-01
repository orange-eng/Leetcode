
# Leetcode practice
# author: orange
# date: 2021/6/1



# 栈方法

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        p = head
        point_num = 0
        while(p is not None):
            point_num += 1
            p = p.next
        if point_num == 0 or point_num == 1:
            return True
        # if point_num % 2 != 0:
        #     return False
        stack = []
        p = head

        if point_num % 2 == 0:
            for i in range(point_num//2):
                stack.append(p.val)
                p = p.next
        else:
            for i in range(point_num//2):
                stack.append(p.val)
                p = p.next
            p = p.next

        while(p is not None):
            number = stack.pop()
            if number == p.val:
                p = p.next
            else:
                return False
        if stack == []:
            return True
        else:
            return False

        


list1 = ListNode()
p = list1
nums = [1]

for i in range(len(nums)):
    p.next = ListNode(nums[i])
    p = p.next

list1 = list1.next


example = Solution()
output = example.isPalindrome(list1)

print(output)