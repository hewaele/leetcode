

class Solution:
    def PredictTheWinner(self, nums):
        n = len(nums)
        small = [[0 for i in range(n)] for j in range(n)]
        big = [[0 for i in range(n)] for j in range(n)]
        i = 0
        for j in range(n):
            small[j][j] = nums[j]
            big[j][j] = 0

        for j in range(n):#r
            i = j-1
            while(i >= 0):#l
                small[i][j] = max(nums[i] + big[i+1][j], nums[j] + big[i][j-1])
                big[i][j] = min(small[i+1][j], small[i][j-1])
                i -= 1

        result = ['Yes' if small[0][-1] >= big[0][-1] else 'No']
        return result[0]




