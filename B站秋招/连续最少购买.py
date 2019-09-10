"""

7 10
1 2 3 4 5 6 7
"""
n, total = map(int, input().strip().split())

show = list(map(int, input().strip().split()))
result = [0]

for i in range(1, n+1):
    result.append(sum(show[:i+1]))

#两种循环的结果
#就算一个摊位是否存在
def fun():
    if total in show:
        return 1
    #判断身上的钱是否大于总价格
    if total > sum(show):
        return -1

    if total == sum(show):
        return n

    min_nums = n+1
    for s in range(1, n):
        for e in range(s+1, n+1):

            if result[e] - result[s-1] == n:
                if e - s + 1 <= min_nums:
                    min_nums = e-s+1

    return min_nums

print(fun())
