# #俄罗斯套娃问题
# 给定一些标记了宽度和高度的信封，宽度和高度以整数对形式 (w, h) 出现。当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。
#
# 请计算最多能有多少个信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。
#
#
# 示例:
#
# 输入: envelopes = [[5,4],[6,4],[6,7],[2,3]]
# 输出: 3
# 解释: 最多信封的个数为 3, 组合为: [2,3] => [5,4] => [6,7]。

class Solution:
    def maxEnvelopes(self, envelopes):
        """
        :param envelopes: 列表
        :return: 一个整数
        """
        #根据第一个属性排序
        envelopes.sort(key=lambda s: (s[0], s[1]))
        #获取长度
        nums1 = 0
        l = -1
        r = -1
        for member in envelopes:
            if member[0] > l and member[1] > r:
                nums1 += 1
                l = member[0]
                r = member[1]
        # print(envelopes)
        # print(nums1)
        # #根据第二个属性排序
        # envelopes.sort(key=lambda s: (s[1], s[0]))
        # print(envelopes)
        # # 获取长度
        # nums2 = 0
        # l = -1
        # r = -1
        # for member in envelopes:
        #     if member[0] > l and member[1] > r:
        #         nums2 += 1
        #         l = member[0]
        #         r = member[1]
        # print(nums2)

        #动态规划求解最长增长序列
        return nums1




if __name__ == '__main__':
    envelopes = [[46,89],[50,53],[52,68],[72,45],[77,81]]
    test = Solution()
    result = test.maxEnvelopes(envelopes)
    print(result)