from collections import Counter
N = int(input())
A = list(map(int,input().split()))
NGF = [-1]*N
count_A = Counter(A)
stack = [0]

for i in range(1,N):
    while stack and count_A[A[stack[-1]]] < count_A[A[i]]:
            NGF[stack.pop()] = A[i]
    stack.append(i)
print(' '.join(map(str,NGF)))
        