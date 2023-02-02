"""
수열의 뒷부분부터 봤을때,
부분수열이 내림차순이라면 해당 부분수열안에서의 변경으로
다음 순열의 모양을 만들 수는 없다.
6 2 1 5 4 3 0 여기선 5 4 3 0
그렇다면 1까지 포함하여 다음 순서를 만들면 된다.
1 5 4 3 0의 다음 순서는 1을 뒤로 보내고 5,4,3,0 중에서 하나를 앞으로 보낸다.
여기서 0은 보낼 수 없는데, 0이 앞으로 가면 다음 순열가 아닌 이전 순열 중에 하나다.
그렇다면 5,4,3 중에 하나를 1과 바꿔야하는데, 1보다 큰 수 중에서 가장 작은 3이 정답이다.
그러므로 1과 3을 스위치! -> 3 5 4 1 0
여기서 제일 앞인 1이 3으로 바뀌였으므로, 그 뒤로는 오름차순이어야한다.
즉, 1 ~~에서 ~~는 가장 커서 1을 3으로 바꾸고, 3 ~~가 되었다.
그러므로 1~~보다 3~~는 사전순에서 다음 순열이지만, 3 ~~에선 가장 처음이 되어야한다.
만약 아니라면, 그건 1 ~~의 다음 순서가 아니다!
그러므로 바꾼 위치인 3 뒤는 전부 오름차순이어야한다.
답 : 6 2 3 0 1 4 5
"""
N = int(input())
sequence = list(map(int,input().split()))

flag = False
for i in range(N-1,0,-1):
    if sequence[i-1] < sequence[i]:
        left = i-1
        flag = True
        break
if flag:
    for i in range(N-1,left,-1):
        if sequence[i] > sequence[left]:
            right = i
            break

    sequence[left],sequence[right] = sequence[right],sequence[left]
    sequence[left+1:] = sorted(sequence[left+1:])
    print(*sequence)
else:
    print(-1)
