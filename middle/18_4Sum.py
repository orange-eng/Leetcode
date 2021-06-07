

# class Solution:
#     def fourSum(self, nums: list, target: int):
#         nums.sort()
#         output = []
#         for i in range(len(nums)-3):
#             low = i+1
#             high = len(nums) - 1 - i

#             while low+1 < high:
#                 for j in range(low+1,high-1):
#                     sum_4 = nums[j] + nums[low] + nums[high] + nums[i] 
#                     if  sum_4 == target:
#                         output.append([j,low,high,i])
#                     if sum_4 < target:
#                         low += 1
#                     else:
#                         high -= 1
#         return output


# 补: setdefault()函数的用法

'''
setdefault方法用于设置key的默认值。该方法接收两个参数，
第1个参数表示key，第2个参数表示默认值。
如果key在字典中不存在，那么setdefault方法会向字典中添加这个key，
并用第2个参数作为key的值。该方法会返回这个默认值。如果未指定第2个参数，
那么key的默认值是None。如果字典中已经存在这个key，
setdefault不会修改key原来的值，而且该方法会返回key原来的值。
'''

class Solution:
    def fourSum(self, nums: list, target: int):
        d = {}
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                d.setdefault(nums[i]+nums[j],[]).append((i,j))
        print(d)

example = Solution()

nums = [1,0,-1,0,-2,2]
output = example.fourSum(nums,0)
#print(output)
            