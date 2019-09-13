"""
2
3
9 8 6
2 3 7

21
"""
m = int(input())
n = int(input())

grap = []
for i in range(m):
    temp = list(map(int, input().strip().split(' ')))

    grap.append(temp)


dp = [[0 for i in range(n+1)] for j in range(m+1)]

#把第一行填了
for i in range(1, m+1):
    for j in range(1, n+1):
        #第一行处理
        if i == 1:
            dp[i][j] = dp[i][j-1] + grap[i-1][j-1]
        #处理第一列
        elif j == 1:
            dp[i][j] = dp[i-1][j] + grap[i-1][j-1]

        else:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grap[i-1][j-1]

# print(dp)
print(dp[-1][-1])