#动态规划解决
"""
输入 n 身上总价格
输入一个序列 表示商品价格 必定存在一个商品价格为1
输出最少商品个数
"""

n = int(input())
price = list(map(int, input().strip(' ').split(' ')))
price = sorted(price)

#构建一个dp矩阵
#这里设置n+1方便后续运算
dp = [[0 for j in range(n+1)] for i in price]

"""
思路：
构建一个二维dp矩阵dp[len(price)][n] 行表示存在的价格数  及price, 对price列表进行从小到大排序方便后续处理
n 表示当前手上的钱
"""

for i in range(len(price)):
    for j in range(n+1):
        #一行一行的填数字
        #填第一行的时候 当前手上的前，只能使用当前的商品价格购买
        if i == 0:
            dp[i][j] = (j+1)/price[i]

        #填完了第一行，开始对第二行往后进行填
        #此时进行状态转移方程的推倒 此时判断当前手上的钱可不可以买当前行的物品，如果不行，那么他的
        #个数应该等于上一行的购买方法
        else:
            if j < price[i]:
                dp[i][j] = dp[i-1][j]
            #如果当前手里的钱大于等于当前行的价格，我们存在两种购买的方式
            #第一种，直接选择上一行的方法 dp[i, j] = d[i-1][j]
            #第二种，选择当前行的商品 dp[i, j] = 1 + dp[i][j-price[i]]
            #主要要理解的地方就是这个 dp[i, j] = 1 + dp[i][j-price[j]]
            #比如我现在在地二行，商品对应的价格是5块，那么前面的4块钱，我都买不起这一行商品，所以只能选择上一行的商品
            #那么前面4个使用的个数就是0 1 2 3 4
            #这是到了第五个商品，我能买了，那对应的选择商品的个数就是1 + dp[1][5-5]
            #两种方法里面我们要选择的就是购买商品最少的那种，所以有
            dp[i][j] = min(dp[i-1][j], 1 + dp[i][j-price[i]])

#输出dp[-1][-1]则为结果
print(dp)
print(dp[-1][-1])

def test(s) -> str:
    print(s)

test('hkjashkdjfha')