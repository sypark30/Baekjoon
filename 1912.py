# 시간 초과
n = int(input())
a = list(map(int, input().split()))
sum_max = a[0]
for i in range(n):
    x = a[i]
    sum_max = max(sum_max, x)
    for j in range(i + 1, n):
        x += a[j]
        sum_max = max(sum_max, x)
print(sum_max)