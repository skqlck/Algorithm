'''
NGE = [-1, -1, ... , -1]로 초기화
스택에 첫번째 원소를 넣고,
A[i]가 stack[-1]의 오큰수라면
    NGE[stack[-1]] = A[i]
    stack.pop()
그 외에는 stack에 Push!
'''
N = int(input())
A = list(map(int,input().split()))
NGE = [-1 for _ in range(N)]
stack = [0]
for i in range(1,N):
    while stack:
        if A[stack[-1]] < A[i]:
            NGE[stack.pop()] = A[i]
        else:
            break
    stack.append(i)
print(' '.join(map(str,NGE)))