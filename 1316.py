def is_group_word(word: str) -> bool:
    for ch in set(word):
        start = word.find(ch)
        # end = word[::-1].find(ch)
        end = word.rfind(ch)
        count = word.count(ch)
        if start + count - 1 != end:
            return False
    return True

n = int(input())
group_word_count = 0
for i in range(n):
    word = input()
    group_word_count += is_group_word(word)
print(group_word_count)