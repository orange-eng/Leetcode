
# Leetcode practice
# author: orange
# date: 2021/6/3

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n ==1:
            return 1
        left = 1
        right = n
        
        while True:
            min = left + (right - left)//2
            if guess(min) == 0:
                return min
            elif guess(min) == -1:
                right = min -1
            elif guess(min) == 1:
                left = min + 1