#输入一组数  求出数当中最大和最大的子数组
"""
输入
-6 5 7 -4 -2 4 6 -8 1 -6 -7 2 -8
输出
5 7 -4 -2 4
"""
arr = list(map(int, input().strip().split()))

dp = [0 for i in range(len(arr)+1)]

for i in range(len(arr)+1):
