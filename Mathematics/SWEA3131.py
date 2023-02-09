prime = [False,True]*(5*10**5)+[False]
prime[0] = False
prime[1] = False
prime[2] = True
for num in range(3,10**6+1,2):
    if prime[num]:
        n = 3
        while num*n < 10**6+1:
            prime[num*n] = False
            n += 2

for i in range(10 ** 6):
    if prime[i]:
        print(i, end=' ')