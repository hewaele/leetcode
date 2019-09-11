#求解
class Solution():
    def __init__(self, queue, k):
        self.queue = queue
        self.k = k
        # self.re = [len(self.queue)-i-1 for i in range(len(self.queue))]

        #构建一个动态规划列表
        #第一问
    def main(self):
        flag = 0
        max = 0
        for index, value in enumerate(self.queue):
            #判断是否为男生，如果是男生，则进行两边扩展
            if value == 'b':
                temp = 0
                #左边扩展
                pos = (index+1)%len(self.queue)
                while(self.queue[pos] == 'g'):
                    temp += 1
                    pos = (pos+1)%len(self.queue)
                #右边扩展
                pos = index - 1
                if pos <= 0:
                    pos = len(self.queue) - 1
                while(self.queue[pos] == 'g'):
                    temp += 1
                    pos = pos-1
                    if pos <= 0:
                        pos = len(self.queue) - 1

                if temp > max:
                    max = temp
                    flag = index
        print(flag)
    #第二问
    def t2(self):
        max = 0
        for index, value in enumerate(self.queue):
            #左边扩展
            pos = index
            num = 0
            k = self.k
            if value == 'g':
                continue

            while(k >= 0):
                if self.queue[pos] == 'b':
                    num += 1
                if self.queue[pos] == 'g':
                    k -= 1
                pos = (pos+1)%len(self.queue)

            if num >= max:
                max = num

        print(max)



test = Solution('bgbbbgbggbgbgbbbbgbgbgbgbgbgbgbgbbggbbgbgbgbgbgbggggbgbgbgbgbgbbggbgbbgbgbbgbgbbgbgbgbgbgbbgbgbgbgbbbb', 20)
test.main()
test.t2()
