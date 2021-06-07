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

- 实例
```python
dict = {'Name': 'Xiaoxiao', 'Age': 18, 'School': 'Hrbeu'}
print (dict.get('School'))
print (dict.get('Sex')
# 输出为：Hrbeu
# 输出为： Nothing
```

# 其他函数

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








 表头  | 表头  | 表头
 ---- | ----- | ------  
 单元格内容  | 单元格内容 | 单元格内容
 单元格内容  | 单元格内容 | 单元格内容  




8、引用
> 第一行引用文字  
> 第二行引用文字
