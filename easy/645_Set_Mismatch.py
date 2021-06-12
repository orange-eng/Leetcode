# Leetcode practice
# author: orange
# date: 2021/6/12


# class Solution:
#     def findErrorNums(self, nums):
#         nums.sort()
#         output = []
#         for i in range(1,len(nums)):
#             if nums[i] == nums[i-1]:
#                 output.append(nums[i])
#         sum_nums_del = sum(nums) - output[0]
#         sum_num = 0
#         for i in range(len(nums)):
#             sum_num += i+1
#         output.append(sum_num-sum_nums_del)
#         return output
class Solution:
    def findErrorNums(self, nums):
        S = sum(set(nums))
        print(S)
        return [sum(nums)-S,len(nums)*(len(nums)+1)//2 -S]


example = Solution()
nums = [1,1]
output = example.findErrorNums(nums)
print(output)