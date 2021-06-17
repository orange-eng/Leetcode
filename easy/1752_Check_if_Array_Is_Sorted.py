



# 失败案例
# 没有考虑到一种情况，数字一样的时候
# class Solution:
#     def check(self, nums):
#         sorted_nums = []

#         for i in range(len(nums)):
#             sorted_nums.append(nums[i])
#         sorted_nums.sort()
        
#         first = sorted_nums[0]  # 可能是一样的
#         index_first = nums.index(first)
#         print(index_first)
#         ans = nums[index_first:] + nums[:(index_first)]
#         if ans == sorted_nums:
#             return True
#         else:
#             return False 


# 成功方法
# 主要在于对最后一位的处理
# 核心步骤 nums[(i+1)%len(nums)]表示最后一位的下一位就是第一位
class Solution:
    def check(self, nums):
        count = 0
        for i in range(len(nums)):
            if nums[i] > nums[(i+1)%len(nums)]:
                count += 1
        return count <= 1



example = Solution()
#nums = [6,10,6]
#nums = [3,4,5,1,2]
nums = [2,1,3,4]
output = example.check(nums)
print(output)