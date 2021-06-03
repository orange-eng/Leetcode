
# Leetcode practice
# author: orange
# date: 2021/6/2




# 方法1
# set集合的用法
'''
a = set([1, 2, 3, 4, 5])
b = set([4, 5, 6, 7, 8])
#求两个集合的交集
print(a & b)
print(a and b)
#求两个集合的并集
print(a | b)
print(a or b)
'''


# 传统方法
# class Solution(object):
#     def intersect(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: List[int]
#         """
#         if nums1 == [] or nums2 == []:
#             return []
#         res = []
#         for i in range(len(nums1)):
#             if nums1[i] in nums2:
#                 res.append(nums1[i])
#                 nums2.remove(nums1[i])
#         return res

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        inter = set(nums1) & set(nums2)
        output = []
        for i in inter:
            for j in range(min(nums1.count(i),nums2.count(i))):
                output.append(i)
        return output

example = Solution()
nums1 = [1,2,2,2]
nums2 = [1,2,2]
output = example.intersect(nums2,nums1)
print(output)
