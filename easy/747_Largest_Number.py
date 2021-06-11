# Leetcode practice
# author: orange
# date: 2021/6/11


class Solution:
    def dominantIndex(self, nums) -> int:
        if len(nums) == 1:
            return 0
        max_number = max(nums)
        index = nums.index(max_number)
        nums.remove(max_number)
        second_number = max(nums)
        if second_number * 2 > max_number:
            return -1
        else:
            return index
        
        

example = Solution()
nums = [3,6,1,0]
output = example.dominantIndex(nums)
print(output)