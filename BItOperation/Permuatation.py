def Permutations(A,r):
    for i in range(len(A)):
        if r == 1:
            yield (A[i],)

        else:
            for next_seq in Permutations(A[:i]+A[i+1:],r-1):
                yield (A[i],)+next_seq

A = list(map(int,input().split()))
r = int(input())

for Permutation in Permutations(A,r):
    print(Permutation)