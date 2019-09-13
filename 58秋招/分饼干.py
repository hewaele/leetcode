"""
样例1
6
3
6
3
5
6
2

10

样例2
10
2
4
2
6
1
7
8
9
2
1

19
"""
n = int(input())

arr = []
for i in range(n):
    arr.append(int(input()))

cookies = [1 for i in range(n)]


for i in range(n):
    #获取第i个孩子连续比他小的人数
    #计算左边
    l = i -1
    lm = 0
    t = arr[i]
    while(l>=0):
        if arr[l] < t:
            t = arr[l]
            lm += 1
            l -= 1
        else:
            break
    #计算右边
    r = i+1
    rm = 0
    t = arr[i]
    while(r < n):
        if arr[r] < t:
            t = arr[r]
            rm += 1
            r += 1
        else:
            break
    cookies[i] += max(lm, rm)

# print(cookies)
print(sum(cookies))

