formula = input()
result = 0
is_subtract = False
for add_formula in formula.split('-'):
    add_sum = 0
    for n in map(int, add_formula.split('+')):
        add_sum += n
    if is_subtract:
        result -= add_sum
    else:
        result += add_sum
        is_subtract = True
print(result)