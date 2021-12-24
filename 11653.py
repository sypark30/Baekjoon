n = int(input())
small_numbers = []
for i in range(2, n + 1):
    while n % i == 0:
        small_numbers.append(i)
        n = int(n / i)
    if n == 1:
        break

for i in small_numbers:
    print(i)