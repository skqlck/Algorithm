# def in_order(now):
#     if now*2+1 < N + 1:
#         return in_order(now*2) + [now] + in_order(now*2+1)
#     elif now*2 < N + 1:
#         return in_order(now*2) + [now]
#     else:
#         return [now]
import sys
sys.stdin = open('input.txt','r')
# for test_case in range(1,11):
#     N = int(input())
#     alphabets = ['']
#     for _ in range(N):
#         n,char,*child = input().split()
#         alphabets.append(char)
#
#     seq = in_order(1)
#     result = ''
#     for s in seq:
#         result += alphabets[s]
#     print(f"#{test_case} {result}")
def inOrder(root):
    global result
    if root*2 < N+1:
        inOrder(root*2)
    result += tree[root]
    if root*2+1 < N+1:
        inOrder(root*2+1)

for test_case in range(1,11):
    N = int(input())
    tree = ['']
    for _ in range(N):
        tree.append(input().split()[1])

    result = ''
    inOrder(1)
    print(f"#{test_case} {result}")
