# 找出1000以内的所有完数
for i in range(2, 7):
    tmp = 0
    for j in range(1, i):
        if i % j == 0:
            tmp += j
        print("i = %d | j = %d | tmp = %d" % (i, j, tmp))
    if i == tmp:
        print(i)
