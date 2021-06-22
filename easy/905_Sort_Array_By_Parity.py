
# Leetcode practice
# author: orange
# date: 2021/6/22


# 奇数和偶数分开存储
# class Solution:
#     def sortArrayByParity(self, nums):
#         print("")
#         odds = []
#         even = []
#         for i in range(len(nums)):
#             if nums[i] % 2 == 0:
#                 even.append(nums[i])
#             else:
#                 odds.append(nums[i])
#         return even +odds

# 交换法
class Solution:
    def sortArrayByParity(self, nums):

        i= 0
        for j in range(len(nums)):
            if nums[j] % 2 == 0:
                nums[i],nums[j] = nums[j],nums[i]
                i += 1
        
        return nums


example = Solution()
nums = [3,1,2,4]
output = example.sortArrayByParity(nums)
print(output)
#print([1]+[2])