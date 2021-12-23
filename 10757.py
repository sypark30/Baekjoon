a, b = input().split()
max_length = max(len(a), len(b))
# while len(a) < max_length:
#     a = "0" + a
# while len(b) < max_length:
#     b = "0" + b
a = "0"*(max_length - len(a)) + a
b = "0"*(max_length - len(b)) + b
# print(f"a={a}")
# print(f"b={b}")

c = ""
second_digit = 0
for i in range(-1, -(max_length + 1), -1):
    sum = second_digit + int(a[i]) + int(b[i])
    first_digit = sum % 10
    second_digit = int(sum / 10)
    c = str(first_digit) + c
if second_digit > 0:
    c = str(second_digit) + c
print(c)