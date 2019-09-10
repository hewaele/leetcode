"""
4
9 6 15 2 -1 12 2 -1 -1 -1 -1 -1 -1 20 37
12 20
"""
h = int(input())
tree = list(map(int, input().strip(' ').split(' ')))
tree = [-1] + tree
c1, c2 = map(int, input().strip(' ').split(' '))

nums = len(tree)
#判断输入是否有效
#中序遍历
order = []
def fun(i):
    if i >= nums:
        return
    fun(2*i)
    if tree[i] != -1:
        order.append(tree[i])
    fun(2*i + 1)

flag = 0
fun(1)
new_order = order[:]
new_order.sort()
print(new_order)
print(order)
if new_order != order:
    flag = 1
    print(-1)


if flag == 0:
    #找到两个结点的父节点列表
    def get_root(c):
        pos = tree.index(c)
        c_father = []
        c_father.append(c)

        while(c != tree[1]):
            pos = pos//2
            c_father.append(tree[pos])
            c = tree[pos]
        return c_father

    c1_father = get_root(c1)
    c2_father = get_root(c2)
    #选择长度短的结点
    if len(c1_father) > len(c2_father):
        c1_father = c1_father[-len(c2_father):]
    if len(c2_father) > len(c1_father):
        c2_father = c2_father[-len(c1_father):]

    flag = 0
    for i in range(len(c1_father)):
        if c2_father[i] == c1_father[i]:
            print(c2_father[i])
            flag = 1
            break

