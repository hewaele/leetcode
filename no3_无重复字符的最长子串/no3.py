"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :param s: 字符串
        :return: 一个整数
        """
        #循环思路
        c = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
             'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']

        max = 0
        for index, val in enumerate(s):
            dic = {}
            temp = 1
            dic[val] = 1
            for next_val in s[index+1:]:
                if next_val not in dic:
                    dic[next_val] = 1
                    temp += 1
                else:
                    break

            if temp >= max:
                max = temp

        return max


test = Solution()
result = test.lengthOfLongestSubstring('pwwkew')
print(result)