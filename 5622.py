dial = {"ABC": 2, "DEF": 3, "GHI": 4, "JKL": 5, "MNO": 6, "PQRS": 7, "TUV": 8, "WXYZ":9}

s = input()
time = 0
for ch in s:
    for key in dial:
        if ch in key:
            number = dial[key]
            break
    time += number + 1
print(time)