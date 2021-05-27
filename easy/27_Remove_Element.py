# Leetcode practice
# author: orange
# date: 2021/5/27

# Leetcode practice
# author: orange
# date: 2021/5/27

# 使用remove函数可以删除数组中的指定元素

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n = len(nums)
        del_num = 0
        i = 0
        while(val in nums):
            nums.remove(val)    # 执行一次remove就删除一个val元素，所以需要多执行几次才可以
        return len(nums)

example = Solution()
nums = [0,1,2,2,3,0,4,2]
val = 2
output = example.removeElement(nums,val)
print(output)
