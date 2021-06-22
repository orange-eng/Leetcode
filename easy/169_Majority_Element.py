# Leetcode practice
# author: orange
# date: 2021/6/22


# 迭代法
# class Solution:
#     def majorityElement(self, nums):
#         output = {}
#         number = 1
#         nums.sort()
#         output[nums[0]] = 1
#         if len(nums) == 1:
#             return nums[0]
#         for i in range(1,len(nums)):
#             if nums[i] == nums[i-1]:
#                 number += 1
#                 if number > len(nums)/2:
#                     return nums[i]

#             else:
#                 output[nums[i-1]] = number
#                 number = 1


# 技巧法
# python3 因为一定有众数，且众数个数大于n/2，所以直接排序输出n/2位置的数即可。[力扣]
class Solution:
    def majorityElement(self, nums):
        nums.sort()
        return nums[int(len(nums)/2)]

example = Solution()
nums = [3,2,2,3,3,2,2]
output = example.majorityElement(nums)
print(output)


# dictary = {1:2,3:4}
# #print(dictary.values())
# max_num = max(dictary.values())
# print(max_num)
# keys = list(dictary.keys())
# values = list(dictary.values())
# idx = values.index(max_num)
# key = keys[idx]
# print("key=",key)

#print(max(dictary.values()))