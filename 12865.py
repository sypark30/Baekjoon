# 시간 초과
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
w_list = []
v_list = []
for i in range(n):
    w, v = map(int, input().split())
    w_list.append(w)
    v_list.append(v)

# 1 : 0b1
# 2 : 0b10
# 3 : 0b11
# 4 : 0b100
# ...
# 15 : 0b1111
v_sum_max = 0
for i in range(1, 2**n):
    w_sum = 0
    v_sum = 0
    bit = 0
    while True:
        binary = (1 << bit)
        if i < binary:
            break
        
        if i & binary != 0:
            w_sum += w_list[bit]
            v_sum += v_list[bit]
        bit += 1
    
    if w_sum <= k:
        v_sum_max = max(v_sum_max, v_sum)

print(v_sum_max)



# import itertools

# n, k = map(int, input().split())
# w_list = []
# v_list = []
# for i in range(n):
#     w, v = map(int, input().split())
#     w_list.append(w)
#     v_list.append(v)
    
# 1 ~ 4 조합
# 1
# 1 2
# 1 3
# 1 4
# 1 2 3
# 1 2 4
# 1 2 3 4
# 2
# 2 3
# 2 4
# 2 3 4
# 3
# 3 4
# 4
# w_sum_list = []
# v_sum_list = []
# for i in range(n):
#     for j in itertools.permutations(w_list, i + 1):
#         w_sum_list.append(j)
#     for j in itertools.permutations(v_list, i + 1):
#         v_sum_list.append(j)

# v_sum_max = 0
# for i in range(len(w_sum_list)):
#     if sum(w_sum_list[i]) > k:
#         continue
#     v_sum_max = max(v_sum_max, sum(v_sum_list[i]))

# print(v_sum_max)