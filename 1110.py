n = input()

old = n
cycle = 0
while True:
    cycle += 1
    if len(old) == 1:
        old = "0" + old
    sum = int(old[0]) + int(old[1])
    new = old[-1] + str(sum)[-1]
    if int(new) == int(n):
        break
    old = new
print(cycle)