
# Leetcode practice
# author: orange
# date: 2021/6/9




# 记录当前位置,以及最远能跳到的位置,逐步更新这两个变量.


class Solution(object):
    def jump(self, nums):
        if len(nums)<2:
            return 0
        count=1;le=len(nums);i=0
        while(i<le-1):
            k=0;ma=0
            if nums[i]+i>=le-1:
                return count
            for j in range(1,nums[i]+1):
                if i+j<le:
                    if nums[i+j]+i+j>=ma:
                        k=i+j
                        ma=nums[k]+k

            i=k
            count+=1
        return count

example = Solution()
nums = [4,1,1,3,1,1,1]
output = example.jump(nums)
print(output)