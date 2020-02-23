var = 1, 2, 3, 4

print(var[1])

print(type(var))

print(1 in var)

list1 = [1, 2, 3, 4, 5, 6, 7]
print(list1)

del list1[1]
print(list1)

list1.append(10)
print(list1)

list1 = list1 + [2]
print(list1.sort())
print(list1)

tup1 = ('Google', 'Runoob', 1997, 2000)
tup2 = (1, 2, 3, 4, 5)
tup3 = "a", "b", "c", "d"  # 不需要括号也可以

# 创建空元组
tup4 = ()

# 元组中的元素值是不允许修改的，但我们可以对元组进行连接组合
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')

# 以下修改元组元素操作是非法的。
# tup1[0] = 100

# 创建一个新的元组
tup3 = tup1 + tup2
print(tup3)

# 复制
print(('Hi!',) * 4)


