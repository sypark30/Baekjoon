croatian_alphabet = ("c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z=")
s = input()

marker = "."
for i in croatian_alphabet:
    s = s.replace(i, marker)
print(len(s))