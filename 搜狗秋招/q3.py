"""
1 2
3 0 1 2
2 1 3
"""

k, rows = map(int, input().strip().split())
#输入rows行
tree = []
for i in range(rows):
    tree.append(list(map(int, input().strip().split())))

#先找到根节点
def find(root):
    for index, t in enumerate(tree):
        if t[1] == root:
            return index
    #没有，则不存在叶子结点 返回-1
    return -1


#宽度遍历
def bfs(root, time):
    #根据k在进行宽度遍历
    #对根节点的子节点个数进行排序，选择子节点个数最多的k个进行宽度遍历
    index = find(root)
    if index == -1:
        result.append(time)
        return
    else:
        for i in tree[index][2:2+k-1]:
            bfs(i, time + 1)


result = []
root = find(0)
bfs(0, 0)
print(max(result))