# Leetcode practice
# author: orange
# date: 2021/5/27

# 使用count函数统计所有元素的个数。
# 使用del函数删除重复出现的元素


class Solution:
    def removeDuplicates(self, nums):
        n = len(nums)
        delNum = 0
        i = 0
        while i < n-delNum:
            if nums.count(nums[i]) != 1:        # count函数用于统计元素及其出现的次数
                del(nums[i])        # 删除这个数组
                delNum += 1
            else:
                i += 1
        return n-delNum

example = Solution()
nums = [1,1,2,2,5,5,5]


output = example.removeDuplicates(nums)
print(output)

# list = ['qwe','xsa','jiu','qwe','xsa','jiu','www','oouy']
# a=set(list)
# for i in a:
# 	num=list.count(i)
# 	print(i,num)
