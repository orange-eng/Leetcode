

# Leetcode practice
# author: orange
# date: 2021/6/4

'''
/*
0         / 2n-2       /  4n-4
1    2n-3   2n-1   4n-5   4n-3
      /       |     /        |
n-2  n      3n-4 /3n-2    5n-4
n-1/        3n-3/         5n-5
j为等处理的字符串的下标，上图为对应下标字符按z字排后的样子，
假设i为行（即从0到n-1），k为某一行的列下标，比如0对应k==0, 2n-2对应k==1，
以行0为例（0, 2n-2,4n-4）等下标j都是2n-2的倍数,其对应下标为j=k*(2n-2)，因为此时的i==0，也就是说k*(2n-2)+i或k*(2n-2)-i都为2n-2的倍数也就是j+i或j-i为2n-2的倍数;
最后一行i对应下标j为 k*(2n-2)+(n-1)，j转换成k*(2n-2)+i比如3n-3==1*(2n-2)-(n-1)==j==k*(2n-2)+i，那么j-i==k*(2n-2),也就是j-i是2n-2的倍数;
中间的行（1到n-2）, 其值与 列*(2n-2)也是有规律的，比如j为2n-3时，行i==1， j+i==2n-3+1==2n-2是k*(2n-2)，表示j+i为2n-2的倍数，另外比如2n-1时j-i=2n-1-1==2n-2是却是表明j-i为2n-2的倍数。
总结一下，首行及尾行满足j-i为2n-2的倍数，中间行满足要么j-i为2n-2的倍数要么j+i为2n-2的倍数。
另外可以发现首行及尾行，每个下标j间相差2n-2, 中间行除了下个下标与之相差2n-2外还多一个数据,
比如i==1行，j==1后面有2n-3, j==1到n-1差n-2==n-1-i,n-1到2n-3间差n-2==n-1-i，二者关系如下(2n-3)==j+(2n-2)-2i
i==1, j==2n-1时后面有4n-5,同理能推导出二者关系如下(4n-5)==j+(2n-2)-2i
根据上面规律i行时，后面会有个i+(2n-2)下标x1外还有一个x2==x1-2i==j+(2n-2)-2i
总结一下，每行的间隔是有规律的，遍历的时候可以直接跳过间隔
*/
'''

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        grid = [[] for _ in range(numRows)]     # 使用二维数组来存储每一行的数据
        # 这里主要考察cycle和Row的数量关系
        #print(grid)
        cycle = 2*numRows - 2 # 循环周期
        for i in range(len(s)):
            pos = i % cycle
            if 0 <= pos <= numRows -1: #Z的一横
                grid[pos].append(s[i])
            else:                       # Z中间的一折
                grid[cycle - pos].append(s[i])
        ans = ''
        for row in grid:
            ans += ''.join(row)

        return ans        
        



example =   Solution()

s = "PAYPALISHIRING" 
numRows = 3

output =  example.convert(s,3)
print(output)