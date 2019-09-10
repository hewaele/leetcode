"""
7
12456 5267
5267 7845
5245 6857
5214 6857

"""
n = int(input())

log = []
for i in range(n):
    s, t = map(int, input().strip().split())
    log.append([s, t])

dic = {}
l_dic = {}
for i in range(n):
    #先创建当前根结点键值 将当前子节点加入他的键值中
    if log[i][0] not in dic:
        dic[log[i][0]] = [log[i][1]]
    else:
        dic[log[i][0]].append(log[i][1])

# print(dic)
m = 0
result = -1
# print(dic)

#循环所有的根节点
def fun(k, t):
    if k not in dic:
        return 1

    for ki in dic[k]:
        t += fun(ki, t)+1

for k, v in dic.items():
    #只要当前结点不再存在叶子结点，则结束
    temp = fun(-1, 0)
    print(temp)
    if temp >= m and k > result:
        result = k


print(result)