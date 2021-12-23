word = input().upper()
d = {}
for ch in word:
    if ch not in d.keys():
        d[ch] = word.count(ch)
        # print(f"d[{ch}]={d[ch]}")

counts = list(d.values())
max_count = max(counts)
if counts.count(max_count) > 1:
    print("?")
else:
    for key in d:
        if d[key] == max_count:
            print(key)
            break