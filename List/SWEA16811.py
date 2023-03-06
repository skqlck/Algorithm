import sys
sys.stdin = open("sample_in.txt","r")
# # 당근을 오름차순 정렬해서 3개 구간으로 쪼개기
# T = int(input())
# for test_case in range(1,1+T):
#     N = int(input())
#     arr = list(map(int,input().split()))
#
#     arr.sort()
#
#     minV = 1000
#     for i in range(N-2):
#         for j in range(i+1,N-1):
#             if arr[i] != arr[i+1] and arr[j] != arr[j+1]:
#                 A = i + 1
#                 B = j - i
#                 C = N - 1 - j
#                 if A*B*C != 0 and A <= N//2 and B <= N//2 and C <= N//2:
#                     if minV > max(A, B, C) - min(A, B, C):
#                         minV = max(A, B, C) - min(A, B, C)
#     if minV == 1000:
#         minV = -1
#     print(f"#{test_case} {minV}")

# # 같은 크기의 당근 개수를 세서, 문제를 해결하는 방법(위와 다르게 같은 크기의 당근이 다른 상자에 들어가는 지 확인 X)
# T = int(input())
# for test_case in range(1,1+T):
#     N = int(input())
#     carrots = [0]*31
#     for carrot in map(int,input().split()):
#         carrots[carrot] += 1
#     minV = 1000
#     for i in range(29):
#         for j in range(30):
#             A = sum(carrots[1:i+1])
#             B = sum(carrots[i+1:j+1])
#             C = sum(carrots[j+1:31])
#             if A*B*C != 0 and A <= N//2 and B<=N//2 and C<=N//2:
#                 diff = max(A,B,C) - min(A,B,C)
#                 if minV > diff:
#                     minV = diff
#     if minV == 1000:
#         minV = -1
#     print(f"#{test_case} {minV}")

# # 개수 누적 합을 이용해서 매번 합을 안해도 되는 경우
# def f(i, j, N):
#     # 누적 안한 경우 A 소, B 중, C 대
#     # A = sum(cnt[1:i + 1])
#     # B = sum(cnt[i + 1:j + 1])
#     # C = sum(cnt[j + 1:31])
#     # 누적한 경우
#     A = cnt[i]
#     B = cnt[j] - cnt[i]
#     C = cnt[30] - cnt[j]
#     if min(A, B, C) == 0:
#         return -1
#     elif max(A, B, C) > N // 2:
#         return -1
#     else:
#         return max(A, B, C) - min(A, B, C)
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     init = 30000
#     minV = init
#     cnt = [0] * 31
#     for x in arr:  # 크기별 개수
#         cnt[x] += 1
#     for i in range(1, 31):
#         cnt[i] = cnt[i] + cnt[i - 1]  # 크기별 개수 누적
#
#     for i in range(1, 29):  # 소 박스 당근 최대 크기
#         for j in range(i + 1, 30):  # 중 박스 당근 최대 크기
#             result = f(i, j, N)  # 포장 시도
#             if result != -1 and minV > result:
#                 minV = result
#     if minV == init:
#         print(f'#{tc} -1')
#     else:
#         print(f'#{tc} {minV}')