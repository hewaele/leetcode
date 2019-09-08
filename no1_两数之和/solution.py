class Solution():
    def twoSum(self, nums, target):

        for index, value in enumerate(nums):
            temp = target - value
            #判断temp是否在list中
            if temp in nums:
                pos = nums.index(temp)
                if pos != index:
                    return [index, pos]

a = [2, 7, 11, 15]
target =9

test = Solution()
print(test.twoSum(a, target))