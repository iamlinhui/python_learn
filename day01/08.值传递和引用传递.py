# 不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
# 可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）

# 它们之间最本质的区别就是在进行参数传递以后改变形式参数的值不同。

# 在值传递中，不改变形式参数的值，而在引用传递中，形式参数的值是被改变的。


# 集合（set）是一个无序的不重复元素序列。

# 可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
import sys


def fixValue(param: set) -> set:
    param.add(12)
    return param


a = set()
fixValue(a)

print(a)

# 可写函数说明
sum = lambda arg1, arg2: arg1 + arg2

# 调用sum函数
print("相加后的值为 : ", sum(10, 20))
print("相加后的值为 : ", sum(20, 20))


print('命令行参数如下:')
for i in sys.argv:
    print(i)
