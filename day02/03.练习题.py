# str1 = 'abcde'
#
# str2 = 'aebced'
#
# print(str1 & str2)

year = 10

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("闰年")
else:
    print("平年")

a = 3
b = 2
c = 1

if a > b:
    t = a
    a = b
    b = t
print("%d %d %d" % (a, b, c))
# 231
if a > c:
    t = a
    a = c
    c = t
print("%d %d %d" % (a, b, c))
# 132
if b > c:
    t = b
    b = c
    c = t
print("%d %d %d" % (a, b, c))
# 123
