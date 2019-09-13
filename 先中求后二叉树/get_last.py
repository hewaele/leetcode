#根据前序中序求出后续
#
# 前序：ABDEFCGH
# 中序：DBFEAGCH
class Solution():
    def __init__(self, pre, mid):
        self.pre = pre
        self.mid = mid
        self.task(0, 0, len(self.pre))

    def task(self, root, s, e):
        """
        :param root: 当前barch的根结点
        :param barch: 分支
        :return:
        """
        #分支长度为1说明该分支已经是叶子结点，将该叶子节点，则结束
        if s >= e:
            return

        #找到根的位置
        for index, leaf in enumerate(self.mid):
            # print(root)
            if leaf == self.pre[root]:
                #将中序序列拆开成两部分
                self.task(root + 1, s, index-1)
                self.task(root + index + 1 - s, index+1, e)
                #把根输出
                print(self.pre[root])
                #退出这个循环

if __name__ == "__main__":
    test = Solution(['A','B','D','E','F','C','G','H'],  ['D','B','F','E','A','G','C','H'])
