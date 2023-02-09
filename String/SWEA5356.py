T = int(input())
for test_case in range(1,1+T):
    words = [input() for _ in range(5)]
    max_length = 0
    for word in words:
        if len(word) > max_length:
            max_length = len(word)

    result = ''
    for idx in range(max_length):
        for word in words:
            if len(word)-1 < idx:
                continue
            result += word[idx]
    print(f"#{test_case} {result}")