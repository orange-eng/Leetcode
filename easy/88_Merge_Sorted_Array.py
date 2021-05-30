

# Leetcode practice
# author: orange
# date: 2021/5/27

# 需要先把两者合并到nums1，然后再进行排序即可

# 注意：
# 不要写return，他自己会返回nums1的
# 要修改nums1，必须保证nums1的id不变


class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2[:n]
        print(nums1)
        sort_myself(nums1)
        #nums1.sort()
        return nums1

def sort_myself(nums):
    temp = 0
    for i in range(len(nums)-1):
        for j in range(i,len(nums)):
            if nums[i] >= nums[j]:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
    return nums

# nums = [1,2,3,2,5,6,1]
# print(sort_myself(nums))


# class Solution(object):
#     def merge(self, nums1, m, nums2, n):
#         """
#         :type nums1: List[int]
#         :type m: int
#         :type nums2: List[int]
#         :type n: int
#         :rtype: None Do not return anything, modify nums1 in-place instead.
#         """
        
#         i = 0
#         j = 0
#         while 0 in nums1:
#             nums1.remove(0)
#         while 0 in nums2:
#             nums2.remove(0)
#         print(nums1)
#         output = []
#         if nums1 == []:
#             return nums2
#         if nums2 == []:
#             return nums1

#         while len(output) != m+n:
#             if nums1[i] < nums2[j] and i<len(nums1) and j<len(nums2):
#                 output.append(nums1[i])
#                 i = i + 1
#             elif nums1[i] >= nums2[j] and i<len(nums1) and j<len(nums2):
#                 output.append(nums2[j])
#                 j =j + 1
#             if i == len(nums1):
#                 a = j
#                 for l in range(len(nums2)-j):
#                     output.append(nums2[a])
#                     a = a + 1
#             if j == len(nums2):
#                 a = i
#                 for _ in range(len(nums1)-i):
#                     output.append(nums1[a])
#                     a = a + 1
#         nums1 = output
#         return nums1

example = Solution()
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
output = example.merge(nums1,3,nums2,3)
print(output)