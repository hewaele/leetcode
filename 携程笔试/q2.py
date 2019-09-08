from sklearn.metrics import roc_auc_score

"""
10
1 0.90
0 0.70
1 0.60
1 0.55
0 0.52
1 0.40
0 0.38
0 0.35
1 0.31
0 0.10

0.68
"""

n = int(input())

result = []
for i in range(n):
    r, p = map(float, input().strip(' ').split(' '))
    result.append([r, p])

result.sort(key=lambda s: s[1])

#计算TPR
#循环判断截断误差
roc = []
for thres in result:
    temp = [int(val[1] >= thres[1]) for val in result]
    #计算tp fn fp tn
    tp = 0
    fn = 0
    fp = 0
    tn = 0
    for index, real in enumerate(result):
        if real[0] == 1 and temp[index] == 1:
            tp += 1
        elif real[0] == 1 and temp[index] == 0:
            fn += 1
        elif real[0] == 0 and temp[index] == 1:
            fp += 1
        elif real[0] == 0 and temp[index] == 0:
            tn += 1
    #得出 tpr fpr
    tpr = tp/(tp+fn)
    fpr = fp/(tn+fp)
    #将结果保存
    roc.append([fpr, tpr])
# print(roc)
roc.reverse()
#计算auc
# print(roc)
last_x = 0
last_y = roc[0][1]
are = 0
for ri in roc[0:]:
    if ri[1] != last_y:
        # print(ri)
        are += (ri[0]-last_x)*last_y
        print(ri[0]-last_x)
        #更新last_y
        last_x = ri[0]
        last_y = ri[1]

are += (roc[-1][0]-last_x)*last_y

print("%.2f"%are)
