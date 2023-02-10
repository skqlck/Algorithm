T = int(input())
for test_case in range(1,1+T):
    word = list(input())
    n = len(word) # 단어 길이
    N = 4*n+1 # 전체 길이
    diamond = [['.' for _ in range(N)] for _ in range(3)]
    for i in range(1,N,2):
        diamond[1][i] = '#'
    for i in range(2,N,4):
        diamond[0][i] = '#'
    diamond.append(diamond[1])
    diamond.append(diamond[0])
    for i in range(N):
        if i%4 == 0:
            diamond[2][i] = '#'
        elif i%2 == 0:
            diamond[2][i] = word.pop(0)
    for line in diamond:
        print(''.join(line))