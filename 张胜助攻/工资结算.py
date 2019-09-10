"""
10 53
100 20000
50 5000
40 1000000
30 700000
20 800000
15 150000
10 1200
8 70000
5 23000
1 200000
"""
#
# m, salary = map(int, input().strip().split())
# total = 0
# temp = []
# for mi in range(m):
#     p, n = map(int, input().split())
#     #将面额大于工资的计算完成
#     if p >= salary:
#         total += n
#     #将面额小于工资存储
#     else:
#         temp += [p for i in range(n)]
#
# #对面额进行排序
# temp.sort(reverse=True)
# residue = sum(temp)
#
# extra = 0
# while(1):
#     #如果面额数组为空 或者剩余面额不足以支付工资，则退出
#     if len(temp) == 0:
#         break
#     if residue < salary:
#         break
#     #循环贪心选择一个面额最大的
#     cur = temp[0]
#     #将第一个删除
#     del(temp[0])
#     while(1):
#         #选择最小的面额
#         # print(temp)
#         cur += temp[-1]
#         del(temp[-1])
#         if cur >= salary:
#             total += 1
#             break
#     residue -= cur
#     extra += cur-salary
#
# print(total)
# print(extra)
a = [[i for i in range(1000000) for j in range(1000000)]]
print(a)
