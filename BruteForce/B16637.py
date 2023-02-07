N = int(input())
A = list(input())
for i in range(0,N,2):
    A[i] = int(A[i])
operations = [i for i in range(1,N-1,2)]
def calculate(A):
    num = A[0]
    idx = 1
    while idx < len(A):
        if A[idx] == '+':
            num += A[idx+1]
        elif A[idx] == '-':
            num -= A[idx+1]
        else:
            num *= A[idx+1]
        idx += 2
    return num

answer = calculate(A)

for i in range(0,1 << (N//2)):
    priorities = []
    for j in range(N//2):
        if i & (1 << j):
            priorities.append(operations[j])

    for priority in priorities:
        if (priority+2 in priorities) or (priority-2 in priorities):
            break
    else: # 괄호가 규칙에 맞게 설정된 상태
        temp = []
        idx = 0
        while idx < N:
            if idx in priorities:
                temp.pop()
                temp.append(calculate(A[idx-1:idx+2]))
                idx += 2
                continue
            temp.append(A[idx])
            idx += 1
        answer = max(answer,calculate(temp))
print(answer)

