def backtrack(A,k,n):

    if k == n: # 부분집합의 원소 선택이 끝났다면
        print(A)
    else:
        k += 1
        for i in range(2):
            A[k] = i
            backtrack(A,k,n)

A = [0,0,0,0]
backtrack(A,0,3)