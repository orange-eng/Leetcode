# Leetcode practice
# author: orange
# date: 2021/6/8



# 神奇的递归法
'''
使用递归来解决该题，主要就是递归的三部曲：

找终止条件：本题终止条件很明显，当递归到链表为空或者链表只剩一个元素的时候，没得交换了，自然就终止了。
找返回值：返回给上一层递归的值应该是已经交换完成后的子链表。
单次的过程：因为递归是重复做一样的事情，所以从宏观上考虑，只用考虑某一步是怎么完成的。
我们假设待交换的俩节点分别为head和next，next的应该接受上一级返回的子链表(参考第2步)。
就相当于是一个含三个节点的链表交换前两个节点，就很简单了，想不明白的画画图就ok。
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        tail = head.next
        head.next = self.swapPairs(tail.next)
        tail.next = head

        return tail

# 定义链表的操作，一定要记住
list1 = ListNode()    #头指针一直没有改变，只是p一直在滑动，并定义了每一个结点的value

nums1 = [1,2,3]

p = list1
for i in range(len(nums1)):
    p.next = ListNode(nums1[i])
    p = p.next
list1 = list1.next

# -----------------------------------------------
example = Solution()
output = example.swapPairs(list1)

p = output
while p is not None:
    print(p.val)
    p = p.next