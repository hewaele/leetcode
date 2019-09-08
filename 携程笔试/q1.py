arr = input()
#构建一个字典
station = {}
t = "abcdefghijklmnopqrstuvwxyz"
for ti in t:
    if ti not in station:
        station[ti] = [-1, -1]

#遍历寻找起点和终点
for index, ri in enumerate(arr):
    #判断作为起点还是终点
    if station[ri][0] == -1:
        station[ri][0] = index
        station[ri][1] = index
    else:
        station[ri][1] = index

#将重复的集合合并
result = []
#将字典转为数组
temp = []
for value in station.values():
    if value[0] == -1:
        continue
    else:
        temp.append(value)
temp.sort(key=lambda s: s[0])
# print(temp)
#定义一个栈存储结果
result = [temp[0]]
for index, value in enumerate(temp[1:]):
    #如果后一个和前一个香蕉，合并他们
    if value[0] <= result[-1][1]:
        result[-1] = [result[-1][0], max(result[-1][1], value[1])]
    else:
        #直接进站
        result.append(value)

#转换结果输出
a = [v[1]-v[0]+1 for v in result]
for i in a[:-1]:
    print(i, end='')
    print(',', end='')
print(a[-1])


