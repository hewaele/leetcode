"""
1,2,2,2,3,4,4
"""
arr = list(map(int, input().strip(' ').split(',')))
new_arr = set(arr)
# print(new_arr)
print(len(new_arr))