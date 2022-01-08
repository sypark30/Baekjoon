# 틀렸습니다 - 반례) 1 1 1 2 2
import sys
input = sys.stdin.readline
n = int(input())

# 직전에 홀수개일때  k
# 1) x, k : (x)
# 2) k, x : (k)

# 직전에 짝수개일때  k, k+1
# 1) x, k, k+1 : (k)
# 2) k, x, k+1 : (x)
# 3) k, k+1, x : (k+1)
x_list = []
for i in range(n):
    x = int(input())
    if x_list:
        is_inserted = False
        for j in range(len(x_list)):
            if x < x_list[j]:
                x_list.insert(j, x)
                is_inserted = True
                break
        if not is_inserted:
            x_list.append(x)
    else:
        x_list.append(x)
        
    length = len(x_list)
    if length <= 2:
        mid = x_list[0]
    elif length == 3:
        mid = x_list[1]
        x_list = [mid]
        
    print(mid)