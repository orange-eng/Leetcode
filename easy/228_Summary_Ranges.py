# Leetcode practice
# author: orange
# date: 2021/6/1




# 类似双指针的思路
# 但是要注意阈值的判断过程

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if nums == []:
            return []
        output = []
        i = 0
        while i < len(nums):
            j = i + 1           # j 为第二个指针
            while j <len(nums) and nums[j] == nums[i] + j -i:
                j = j + 1
            if i == j-1:
                output.append(str(nums[i])) 
            else:
                output.append(str(nums[i]) + '->' + str(nums[j-1]))
            i = j
        return output

example = Solution()

list1 = [1,2,3,4,6]

output = example.summaryRanges(list1)
print(output)
