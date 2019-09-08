
x = int(input())
#传入 f1 f2
dic = {}

def fun(f1, f2, x):
    #计算直到x出现
    pos = 3
    while(1):
        f3 = f1 + f2

        #判断f3是否相等或者大于这退出
        if f3 == x:
            # print(f1, f2, f3)
            #判断pos是否存在 存在则加1 不存在设为1
            if str(pos) in dic:
                dic[str(pos)] += 1
            else:
                dic[str(pos)] = 1
                #结束循环
            return

        if f3 > x:
            return

        f1 = f2
        f2 = f3
        pos += 1

for i in range(1, x):
    for j in range(1, x-i):
        fun(i, j, x)

temp = []
for key, value in dic.items():
    temp.append([int(key), value])

temp.sort(key= lambda s: s[0])
for row in temp:
    print("{} {}".format(row[0], row[1]))