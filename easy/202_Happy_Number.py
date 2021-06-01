
'''
//参考英文网站热评第一。这题可以用快慢指针的思想去做，有点类似于检测是否为环形链表那道题
//如果给定的数字最后会一直循环重复，那么快的指针（值）一定会追上慢的指针（值），也就是
//两者一定会相等。如果没有循环重复，那么最后快慢指针也会相等，且都等于1。
'''


# 快慢指针方法
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        def get_digits(num):
            output = 0

            while num != 0:
                output = output + pow(num%10,2)
                num = num // 10

            return output
        fast = 0
        slow = 0
        slow = get_digits(n)
        fast = get_digits(n)
        fast = get_digits(fast)
        while(slow != fast):
            slow = get_digits(slow)
            fast = get_digits(fast)
            fast = get_digits(fast)
            print(slow)

        if fast == 1:
            return True
        else:
            return False

example = Solution()

output = example.isHappy(7)
print(output)

        