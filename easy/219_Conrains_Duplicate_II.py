# Leetcode practice
# author: orange
# date: 2021/6/1

# 创建字典，然后查找即可


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) <= 1:
            return False
        dictatory = {}

        for i in range(len(nums)):

            if nums[i] in dictatory:
                if i - dictatory[nums[i]] <= k:     #dict查找时，一定查找最后一个
                    return True
            dictatory[nums[i]] = i
        return False
example = Solution()

nums = [1,2,3,1,1]
k = 2
output = example.containsNearbyDuplicate(nums,k)
print(output)


MY_DICT = {1:1,2:2,2:10,3:3,1:4,1:5}
print(MY_DICT[2])