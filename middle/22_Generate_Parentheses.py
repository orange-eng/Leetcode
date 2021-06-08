# Leetcode practice
# author: orange
# date: 2021/6/8



# 递归法（还是学不会呀）

class Solution:
    def generateParenthesis(self, n: int):
        ans = []

        def DFS(s,L,R):
            if L<R or L>n or R>n:
                return
            if L == n and R == n:
                ans.append(str(s))
                return
            # 左括号
            DFS(s+"(",L+1,R)
            # 右括号
            DFS(s+")",L,R+1)
        
        DFS("",0,0)
        return ans

example = Solution()
output = example.generateParenthesis(2)
print(output)
