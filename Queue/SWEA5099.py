T = int(input())
for test_case in range(1, 1 + T):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))
    p_idx = 0
    queue = [-1] * N
    q_idx = 0
    out_cnt = 0
    while out_cnt != M - 1:
        if queue[q_idx] == -1:
            if p_idx < M:
                queue[q_idx] = [p_idx, pizza[p_idx] // 2]
                p_idx += 1
        elif queue[q_idx][1] == 0:
            queue[q_idx] = -1
            out_cnt += 1
            continue

        elif queue[q_idx][1] != 0:
            queue[q_idx][1] //= 2

        q_idx = (q_idx + 1) % N

    for item in queue:
        if item != -1:
            print(f"#{test_case} {item[0] + 1}")