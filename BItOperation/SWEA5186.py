T = int(input())
for test_case in range(1,1+T):
    N = float(input())
    answer = ""
    cnt = 1
    while N > 0:
        if N - 2**(-cnt) >= 0:
            N -= 2**(-cnt)
            answer += "1"
            cnt += 1
        else:
            cnt += 1
            answer += "0"

        if len(answer) >= 13:
            print(f"#{test_case} overflow")
            break
    else:
        print(f"#{test_case} {answer}")