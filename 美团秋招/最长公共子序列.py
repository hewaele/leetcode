n1 = int(input())
arr1 = list(map(int, input().strip().split()))
n2 = int(input())
arr2 = list(map(int, input().strip().split()))

def find_set(s1, s2):
    dp = [[0 for i in range(len(s2)+1)] for j in range(len(s1)+1)]
    max = 0

    # print(len(s2))

    for i in range(len(s1)):
        for j in range(len(s2)):
            # print(i+1, j+1)
            if s1[i] == s2[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            if dp[i+1][j+1] > max:
                max = dp[i+1][j+1]

    return max

result = find_set(arr1, arr2)
print(result)
