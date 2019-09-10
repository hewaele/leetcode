a = list(input().strip().split(','))

#要解决0的问题
for index, v in enumerate(a):
    a[index] += a[index][0]
a.sort(reverse=True)
# print(a)
for index, v in enumerate(a):
    a[index] = a[index][:-1]
# print(a)
print(''.join(a))