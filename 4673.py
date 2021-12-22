def d(n):
    sum = n
    for ch in str(n):
        sum += int(ch)
    return sum

# import time

# start = time.time()

num = 10000
numbers = list(range(1, num + 1))
not_self_numbers = {}
for n in numbers:
    next = d(n)
    # print(f"{n} -> {next}")
    not_self_numbers[next] = None

self_numbers_set = set(numbers) - set(not_self_numbers.keys())
self_numbers = list(self_numbers_set)
self_numbers.sort()
for i in self_numbers:
    print(i)

# Dictionary 대신 List로.
# num = 10000
# numbers = list(range(1, num + 1))
# not_self_numbers = []
# for n in numbers:
#     next = d(n)
#     # print(f"{n} -> {next}")
#     not_self_numbers.append(next)

# self_numbers_set = set(numbers) - set(not_self_numbers)
# self_numbers = list(self_numbers_set)
# self_numbers.sort()
# for i in self_numbers:
#     print(i)
    
# print(f"elapsed : {time.time() - start}")

