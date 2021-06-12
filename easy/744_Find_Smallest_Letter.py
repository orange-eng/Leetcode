
# Leetcode practice
# author: orange
# date: 2021/6/12

# 简单题目

class Solution:
    def nextGreatestLetter(self, letters, target: str):
        for i in range(len(letters)):
            if letters[i] > target:
                return letters[i]
        
        return letters[0]

example = Solution()
letters = ["c","f","j"]
target = "g"
output = example.nextGreatestLetter(letters,target)
print(output)