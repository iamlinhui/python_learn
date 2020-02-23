num = 3
i = 2
flag = False
while i < num:
    if num % i == 0:
        flag = False
        break
    else:
        flag = True
    i += 1

if flag or num == 1 or num == 2:
    print("质数")
else:
    print("非质数")
