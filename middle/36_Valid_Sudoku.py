
# Leetcode practice
# author: orange
# date: 2021/6/8



'''
使用line,column,和子区域来分别保存元素,如果元素有重复的就返回false,否则返回true即可. 
在这里巧用了一下集合. 判断某个元素是否在集合中时间复杂度是O(1),如果使用列表的话就是O(n)了. 
其中划分子区域的技巧很巧妙,使用的是 pos = (i//3)*3 + j//3
'''

class Solution:
    def isValidSudoku(self, board) -> bool:
        matrix_line = [set() for i in range(9)]
        matrix_column = [set() for i in range(9)]
        matrix_area = [set() for i in range(9)]
        for i in range(9):
            for j in range(9):
                item = board[i][j]
                pos = (i//3)*3 + j //3          #给子区域进行编号
                if item != '.':
                    if item not in matrix_line[i] and item not in matrix_column[j] and item not in matrix_area[pos]:
                        matrix_line[i].add(item)
                        matrix_column[j].add(item)
                        matrix_area[pos].add(item)
                    else:
                        return False
        print(matrix_area)
        return True


board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

example = Solution()
output = example.isValidSudoku(board)
print(output)