def is_prime_number(n: int) -> bool:
    if n == 1: 
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

m, n = map(int, input().split())
for i in range(m, n + 1):
    if is_prime_number(i):
        print(i)

# 시간 줄이려고 시도했으나, 틀림..
# m, n = map(int, input().split())
# prime_numbers = []
# # m - 1까지 소수 찾기
# for i in range(2, m):
#     is_prime_number = True
#     for j in range(2, int(i**0.5) + 1):
#         if i % j == 0:
#             is_prime_number = False
#             break
#     if not is_prime_number:
#         continue
#     prime_numbers.append(i)
#     # print(i)

# # m ~ n 중 소수 찾기
# for i in range(m, n + 1):
#     is_prime_number = True
#     # 현재까지 찾은 소수들로 확인
#     for j in prime_numbers:
#         if j > int(i**0.5):
#             break
#         if i % j == 0:
#             is_prime_number = False
#             break
#     if not is_prime_number:
#         continue
    
#     # 이후 숫자들로 소수 확인 필요 없음?
#     # next = 2
#     # if len(prime_numbers) > 0:
#     #     next = prime_numbers[-1] + 1
#     # for j in range(next, i):
#     #     if i % j == 0:
#     #         is_prime_number = False
#     #         break
#     # if not is_prime_number:
#     #     continue
#     prime_numbers.append(i)
#     print(i)