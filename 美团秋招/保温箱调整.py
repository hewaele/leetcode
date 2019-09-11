"""

5
3 3 0 3 4 7 4 1
4 7 6 5 6 8 5 5

4
4 3 1 4 5
7 6 6 5 5
"""

n = int(input())
a = list(map(int, input().strip().split()))
b = list(map(int, input().strip().split()))

#在保证保温箱最少的情况下，求最少时间
total = sum(a)
# print(total)
#对b进行排序，选择最大的
c = [[i, j] for i, j in zip(a, b)]
c.sort(key=lambda s:(s[1], s[0]), reverse=True)

#循环选择，直到最大
t = []
add = 0
pos = 0

for index, [ai, bi] in enumerate(c):
    add += bi
    if add >= total:
        add -= bi
        pos = index
        break

    t.append([ai, bi])

#循环选择当前可行方案，同时已经含有的个数最多的
m = 0
# print(t)
flag = []
for ci in c[pos:]:
    if add + ci[1] >= total and ci[0] >= m:
        m = ci[0]
        flag = ci
    # if add + ci[0] < total:
    #     break

#将最后一个加入到t
t.append(flag)
#计算当前选择的箱子的外卖个数
# print(t)
l = len(t)
print(t)
time = 0
for ti in t:
    time += ti[0]

print("%d %d"%(l, total-time))



