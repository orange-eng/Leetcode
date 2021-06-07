
# Leetcode practice
# author: orange
# date: 2021/6/4

'''
这里用到了动态规划，基本的表达式: area = min(height[i], height[j]) * (j - i) 
使用两个指针，值小的指针向内移动，这样就减小了搜索空间 
因为面积取决于指针的距离与值小的值乘积，如果值大的值向内移动，距离一定减小，
而求面积的另外一个乘数一定小于等于值小的值，因此面积一定减小，
而我们要求最大的面积，因此值大的指针不动，而值小的指针向内移动遍历
'''



class Solution:
    def maxArea(self, height):
        front = 0
        behind = len(height) - 1
        max_container = 0
        while(front < behind):
            if height[front] < height[behind]:
                min_height = height[front]
                max_container = max(max_container,(behind - front)*min_height)
                front += 1
            else:
                min_height = height[behind]
                max_container = max(max_container,(behind - front)*min_height)
                behind -= 1

            #print("max_container=",max_container)
        return max_container

example = Solution()

height = [1,2,1]
output = example.maxArea(height)
print(output)
