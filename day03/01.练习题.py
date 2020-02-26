# 找出1000以内的所有完数
for i in range(2, 1000):
    tmp = 0
    for j in range(1, i):
        if i % j == 0:
            tmp += j
    if i == tmp:
        print(i)
