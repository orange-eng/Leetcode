# Leetcode
- 该部分简单记录一些常用的python内置函数，在刷题时会经常使用到。

# 删除元素
## del 函数

del用于list列表操作，删除一个或者连续几个元素。

例：定义一个list型数据，data = [1,2,3,4,5,6]
1.del(data):删除整个list。
2.del(data[i]):删除data中索引为i个数据
3.del(data[i:j]):删除data中第i个数据到第j个数据之前（不含j）的数据

## remove 函数

- **描述**  
删除列表中的给定的对象
- **语法**  
list.remove()
- **参数**  
obj 参数（可选择性插入）obj的作用是要从列表中删除的对象的索引

使用如：list.remove(obj = list[0])  
返回值
remove方法删除后不会返回值

- 代码
```python
list = [1, 2, 3, 4, 5]
list.remove(1)
print (list)
#输出结果为：[2, 3, 4, 5]

list.remove(5)
print(list)
#输出结果为：[2, 3, 4]
```

## pop 函数

- 利用pop()方法弹出元素，当（）内无索引数时默认弹出最后一个元素

```python
x = ['a', 'b', 'c', 'd']
x.pop(2)
print x

#结果为['a', 'b', 'd']
```

# 查找索引

## index() 函数

- **描述**
index() 函数用于从列表中找出某个值第一个匹配项的索引位置。

- **语法**  
list.index(x[, start[, end]])

- **参数**
x-- 查找的对象。
start-- 可选，查找的起始位置。
end-- 可选，查找的结束位置。

- **返回值**
该方法返回查找对象的索引位置，如果没有找到对象则抛出异常。

```python
A = [123, 'xyz', 'zara', 'abc']

print(A.index('xyz'))  # 结果 1
print(A.index('zzz'))  # 报错 ：ValueError: 'zzz' is not in list
```


## find() 函数

- **描述**  
find() 方法检测字符串中是否包含子字符串 str

- **参数**  
str -- 指定检索的字符串  
beg -- 开始索引，默认为0  
end -- 结束索引，默认为字符串的长度。

```python

>>>info = 'abca'
>>> print info.find('a')    # 从下标0开始，查找在字符串里第一个出现的子串，返回结果：0
0
>>> print info.find('a',1)  # 从下标1开始，查找在字符串里第一个出现的子串：返回结果3
3
>>> print info.find('3')    # 查找不到返回-1
-1

```



# 计数

## count() 函数

- **描述**  
count() 方法用于统计字符串里某个字符出现的次数。可选参数为在字符串搜索的开始与结束位置

- **参数**  
sub -- 搜索的子字符串  
start -- 字符串开始搜索的位置。默认为第一个字符,第一个字符索引值为0。  
end -- 字符串中结束搜索的位置。字符中第一个字符的索引为 0。默认为字符串的最后一个位置。

- **返回值**  
该方法返回子字符串在字符串中出现的次数。

```python
>>> "MacBook Pro".count("o", 5)
2
```

## Counter()函数
- **描述**
counter()作用就是在一个数组内，遍历所有元素，将元素出现的次数记下来
```python
a = [1,4,2,3,2,3,4,2]  
from collections import Counter  
print Counter(a)

#结果为：Counter({2: 3, 4: 2, 3: 2, 1: 1})
```  


# 去重

## set方法
- 这个比较简单，直接看代码即可
```python
# 由于数据类型set本身具有无序，唯一值的特性，可以用内置函数set对字符串和列表进行去重，挺方便的
str = "asdfasdlklfgklgjsdfjkjl"
se = set(str)       # 变为集合set，已经不是列表list
print (se)          # {'j', 'f', 'a', 'd', 'l', 's', 'g', 'k'}
str = list(se)      # 再变为列表list
print(str)          # ['j', 'f', 'a', 'd', 'l', 's', 'g', 'k']
```


# 字典

## get()函数
- get()用于返回指定键的值，如果不在字典中，那么返回默认值

- **参数**  
```python
dict.get(key, default=None)
```
key：字典中要查找的键。  
default：可选参数，如果指定键的值不存在时，返回该值，默认为 None。


# 循环函数
在执行 while 循环或者 for 循环时，只要循环条件满足，程序将会一直执行循环体，不停地转圈。但在某些场景，我们可能希望在循环结束前就手动离开循环，Pyhton 提供了 2 种强制离开当前循环体的办法：

- 使用 continue 语句，可以跳过执行本次循环体中剩余的代码，转而执行下一次的循环。
- 只用 break 语句，可以完全终止当前循环。


## continue函数
- **概述**
continue 语句用来告诉Python跳过当前循环的剩余语句，然后继续进行下一轮循环。

- **实例**
```python
dict = {'Name': 'Xiaoxiao', 'Age': 18, 'School': 'Hrbeu'}
print (dict.get('School'))
print ("")
```
- **实例**
```python
for letter in 'Python':     # 第一个实例
   if letter == 'h':
      continue
   print('当前字母 :', letter)

   Output:
   ----------------
   当前字母 : P
   当前字母 : y
   当前字母 : t
   当前字母 : o
   当前字母 : n
```

## break函数
- **概述**  
break 用于完全结束一个循环，跳出循环体。不管是哪种循环，一旦在循环体中遇到 break，系统就将完全结束该循环，开始执行循环之后的代码。

- break 语句一般会结合 if 语句进行搭配使用，表示在某种条件下，跳出循环体，如果使用嵌套循环，break 语句将跳出当前的循环体。

- ** 实例**
```python
for i in range(0, 10) :
    print("i的值是: ", i)
    if i == 2 :
        # 执行该语句时将结束循环
        break
output:
i的值是:  0
i的值是:  1
i的值是:  2
```

# 其他函数

## map()函数
map是python内置函数，会根据提供的函数对指定的序列做映射
```python
map(function,iterable,...)
```
第一个参数接受一个函数名，后面的参数接受一个或多个可迭代的序列，返回的是一个集合。

把函数依次作用在list中的每一个元素上，得到一个新的list并返回。注意，map不改变原list，而是返回一个新list。

- 实例1

```python

del square(x):
    return x ** 2

map(square,[1,2,3,4,5])

# 结果如下:
[1,4,9,16,25]

```
- 实例2
```python
class Solution:
    def countLargestGroup(self, n: int) -> int:
        # 分解做法
        # 1.求每个数字的数位和
        sum_list = list(map(lambda x: sum(map(int, str(x+1))), range(n)))
        # 2. 记录每个和出现的次数
        c_list = Counter(sum_list).values()
        # 3. 记录每个和出现的次数进行计数
        s_list = Counter(c_list).items()
        # 4. 返回数字数目并列最多的组的次数，因此是[1]
        return max(s_list)[1]
```


## tuple()函数

- 描述

 tuple()函数用于将列表、区间（range）等转换为元组。

注意：元组和列表非常类似，但列表与元组最大的区别在于：元组是不可改变的，列表是可改变的。元组支持的操作，列表基本上都支持；列表支持对元素的修改，而元组则不支持。从这个角度来看，可以认为列表是增强版的元组。

虽然大部分时候都可使用列表来代替元组，但如果程序不需要修改列表所包含的元素，那么使用元组代替列表会更安全。

```python

a = [1,2] #list
b = {"1":2,"3":3} #dict
c = {1,2,3,3}  #set
d = range(2,10,2) #range
print(tuple(a))
print(tuple(b))
print(tuple(c))
print(tuple(d))
```
output:
```python
(1, 2)
('1', '3')
(1, 2, 3)
(2, 4, 6, 8)
```



# 常用方法

## 牛顿迭代法
- 牛顿迭代法几乎可以求解所有的方程组，其迭代公式也十分简单，经常使用。

- 公式为： Xn+1 = Xn -f(x)/f'(x)

### 实例：求解平方根

f(x) = x^(2) - a
y^2 = x
yn+1 = yn - (yn^2 - x)/2yn
r = r - (r^2 - x)/2r
**代码如下**
```python
# 牛顿迭代法
#y^2 = x
#迭代公式为yn+1 = yn -(yn^2 - x)/(2yn)

class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 1:
            return x
        r = x
        while r > x / r:                # 设置好临界条件
            r = (r + x / r) // 2        # 根据牛顿迭代法求出递推公式
            # r = (2*r + x/(r*r))//3
        return int(r)
```






 表头  | 表头  | 表头
 ---- | ----- | ------  
 单元格内容  | 单元格内容 | 单元格内容
 单元格内容  | 单元格内容 | 单元格内容  




8、引用
> 第一行引用文字  
> 第二行引用文字
