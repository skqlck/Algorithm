import time
import sys
sys.setrecursionlimit(10000)
def measure_running_time(func):
    def wrapper(n):
        start = time.time()
        result = func(n)
        end = time.time()
        print(f"Running time = {end-start}")
        return result

    return wrapper

def memoization(func):
    cache = [0]*10000
    cache[1] = 1
    def wrapper(n):
        if n > 1 and cache[n] == 0:
            cache[n] = func(n)
        return cache[n]

    return wrapper
@memoization
def fibo1(n):
    if n < 2:
        return n
    return fibo1(n-1) + fibo1(n-2)

def fibo2(n):
    if n < 2:
        return n
    return fibo2(n - 1)+fibo2(n - 2)


print(measure_running_time(fibo1)(30))
print(measure_running_time(fibo2)(30))