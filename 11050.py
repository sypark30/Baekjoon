def factorial(n: int) -> int:
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

n, k = map(int, input().split())
result = factorial(n) // (factorial(k) * factorial(n - k))
print(result)