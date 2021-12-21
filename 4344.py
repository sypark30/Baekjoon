c = int(input())
for i in range(c):
    scores = list(map(int, input().split()))[1:]
    average = sum(scores) / len(scores)
    upper_count = len(list(filter(lambda score: score > average, scores)))
    print(f"{upper_count / len(scores):.3%}")