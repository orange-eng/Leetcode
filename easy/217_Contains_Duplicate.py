# Leetcode practice
# author: orange
# date: 2021/6/1


#python自带去重功能set()函数



class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(set(nums)) != len(nums)


alist=[1,2,2,4,4,6,7]
b=set(alist)
print(list(b))