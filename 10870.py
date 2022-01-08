a = {0: 0, 1: 1}
def fibonacci(n: int) -> int:
    if n in a:
        return a[n]
    else:
        fn_1 = fibonacci(n - 1)
        fn_2 = fibonacci(n - 2)
        fn = fn_1 + fn_2
        # print(f"{n} : {fn}")
        a[n] = fn
        return fn

n = int(input())
answer = fibonacci(n)
print(answer)