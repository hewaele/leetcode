"""

3
4 5 -7 1 -4 8 6 4 8
"""
import os
import sys
import numpy as np

n = int(input())
arr = list(map(int, input().strip().split()))

new_arr = []
#将数组改成矩阵形式
for i in range(n):
    temp = arr[i*n:(i+1)*n]
    new_arr.append(temp)
new_arr = np.array(new_arr)

dp = [[0 for i in range(n+1) for j in range(n+1)]]

#对dp进行填表
for i, row in enumerate(new_arr):
    for j, v in enumerate(row):
        if i != 0 and j != 0:
            dp[i][j] = dp[i-1][j] + dp[i][j-1] + v

#二重循环寻找最大值
m = -129*200

for i in range(1, n+1):
    for j in range(1, n+1):
        #计算当前结点
        pass




