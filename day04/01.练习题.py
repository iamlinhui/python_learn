# 结果收集器
resultNameCount = {}

fileName = "name.txt"
file = open(fileName)

line = file.readline()

while line:
    surname = line.split(" ")[0]
    currentCount = resultNameCount.get(surname)
    if currentCount is None:
        resultNameCount[surname] = 1
    else:
        currentCount += 1
        resultNameCount[surname] = currentCount

    line = file.readline()

# 输出结果
for item in resultNameCount:
    print("姓氏：%s 出现的个数：%d" % (item, resultNameCount[item]))
