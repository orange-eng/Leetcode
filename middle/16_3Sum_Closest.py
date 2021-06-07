
# Leetcode practice
# author: orange
# date: 2021/6/7



class Solution:
    def threeSumClosest(self, nums: list, target: int) -> int:
        n = len(nums)
        nums.sort()
        re_min = 0      # 存储当前最小的差值
        for i in range(n):
            low = i + 1
            high = n - 1
            while low < high:
                three_sum = nums[low] + nums[high] +nums[i]
                x = target - three_sum      # 当前三个数之和的差值

                if re_min == 0:             # 第一次循环时
                    re_min = abs(x)
                    sum_min = three_sum     # sum_min为当前最接近的和
                
                if abs(x) < re_min:         # 如果差值减小，才会更新sum_min
                    re_min = abs(x)
                    sum_min = three_sum
                
                if three_sum == target:
                    return target
                elif three_sum < target:
                    low += 1
                else:
                    high -= 1
                
        return sum_min

example = Solution()
nums = [-1,2,1,-4]
output = example.threeSumClosest(nums,1)
print(output)

