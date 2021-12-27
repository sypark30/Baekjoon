# n = int(input())
# numbers = []
# for i in range(n):
#     x = int(input())
#     is_added = False
#     if numbers:
#         for index in range(len(numbers)):
#             if x < numbers[index]:
#                 numbers.insert(index, x)
#                 is_added = True
#                 break
#     if not is_added:
#         numbers.append(x)
    
# for number in numbers:
#     print(number)


# Python 3로는 시간 초과로 실패, PyPy3에서 성공
# sort 보다는 input, print에서 시간 초과가 되는 듯?
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))
    
numbers.sort()

for number in numbers:
    print(number)