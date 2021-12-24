def is_prime_number(n: int) -> bool:
    if n == 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n = int(input())
numbers = map(int, input().split())
prime_numbers = list(filter(is_prime_number, numbers))
# print(prime_numbers)
print(len(prime_numbers))