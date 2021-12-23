t = int(input())
for i in range(t):
    x, y = map(int, input().split())
    distance = y - x
    # 1 : 1
    # 2 : 1 1
    # 3 : 1 1 1
    # 4 : 1 2 1
    # 5 : 1 2 1 1
    # 6 : 1 2 2 1
    # 7 : 1 2 2 1 1
    # 8 : 1 2 2 2 1
    # 9 : 1 2 3 2 1
    # 10 : 1 2 3 2 1 1
    # 11 : 1 2 3 2 2 1
    # 12 : 1 2 3 3 2 1
    # 13 : 1 2 3 3 2 1 1
    # 14 : 1 2 3 3 2 2 1
    # 15 : 1 2 3 3 3 2 1
    # 16 : 1 2 3 4 3 2 1
    # 17 : 1 2 3 4 3 2 1 1
    # ...
    # 20 : 1 2 3 4 4 3 2 1
    # 21 : 1 2 3 4 4 3 2 1 1
    # ...
    # 25 : 1 2 3 4 5 4 3 2 1
    
    # 25 : 5*5 -> 9 = 5+5-1
    # 20 : 4*5 -> 8 = 4+5-1
    # 16 : 4*4 -> 7 = 4+4-1
    # 12 : 3*4 -> 6 = 3+4-1
    #  9 : 3*3 -> 5 = 3+3-1
    #  6 : 2*3 -> 4 = 2+3-1
    #  4 : 2*2 -> 3 = 2+2-1
    #  2 : 1*2 -> 2 = 1+2-1
    #  1 : 1*1 -> 1 = 1+1-1
    import math
    root = math.sqrt(distance)
    root_floor = math.floor(root)
    root_ceil = math.ceil(root)
    if distance <= root_floor * root_ceil:
        count = root_floor + root_ceil - 1
    else:
        count = root_floor + root_ceil
    print(count)