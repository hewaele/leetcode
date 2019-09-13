#根据前序中序求出后续
"""
中
后

dgbaechf
gbdehfca
"""
result = []
class Solution():
    def __init__(self, mid, last):
        self.last = last
        self.mid = mid
        self.task(len(self.last) - 1, 0, len(self.last)-1)

    def task(self, root, s, e):
        """
        :param root: 当前barch的根结点
        :param barch: 分支
        :return:
        """
        #分支长度为1说明该分支已经是叶子结点，将该叶子节点，则结束
        if s > e:
            return

        #找到根的位置
        for index, leaf in enumerate(self.mid):
            #像输出根
            if leaf == self.last[root]:
                result.append(leaf)
                #将中序序列拆开成两部分 左边和右边
                #左边 根结点为
                self.task(root - (e - index) - 1, s, index-1)
                self.task(root - 1, index+1, e)

mid = input()
pre = input()
test = Solution(mid,  pre)
print(''.join(result))
