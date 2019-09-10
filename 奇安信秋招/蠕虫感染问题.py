n = int(input())
graph = []
for i in range(n):
    temp = list(map(int, input().strip().split()))
    graph.append(temp)

bug = list(map(int, input().strip().split()))
bug.sort(reverse=True)

result = {}
#循环判断厨师被感染的结点 选择连接数最多的那个
m = -1
index = n+1
for node in bug:
    gr = sum(graph[node]) - 1
    if gr >= m:
        m = gr
        index = node

print(index)
