'''
S와 A_i들의 차이를 d_i라고 했을 때,
d_i들의 최대공약수가 문제에서 찾는 D이다.

GCD
* 두 자연수 a,b (a < b) 에 대하여 a,b의 최대공약수는 a,b-a의 최대공약수와 같다.
* 즉, a,b의 최대공약수는 a,b%a의 최대공약수와 같다.
'''
def GCD(a,b):
    a,b = sorted([a,b])
    while a:
        a,b = b%a,a
    return b

N,S = map(int,input().split())
A = list(map(lambda x: abs(int(x)-S),input().split()))
answer = A[0]
for i in range(1,N):
    answer = GCD(answer,A[i])
print(answer)