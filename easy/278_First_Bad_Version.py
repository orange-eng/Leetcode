
# Leetcode practice
# author: orange
# date: 2021/6/2




# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        high = n
        mid = 0
        if n == 1:
            return 1
        while(low < high):
            mid = low + (high - low)/2
            if isBadVersion(mid):
                high = mid
            else:
                low = mid + 1
        

        return high