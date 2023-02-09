# skip을 pattern의 [i]번째 문자가 처음 나온 인덱스+1?
def Boyer_Moore(text,pattern):
    N, M = len(text), len(pattern)
    skip = [M]*128
    for i in range(M-1):
        skip[ord(pattern[i])] = (M-1) - i

    i = 0 # text index
    while i < N-M+1:
        j = M - 1  # pattern index
        while j > -1 and text[i+j] == pattern[j]:
            j -= 1
        if j == -1:
            return i
        i += skip[ord(text[i+j])]

    return -1

# text = input()
# pattern = input()
# answer = Boyer_Moore(text,pattern)
# print(answer)

text = input()
pattern = input()
answer = Boyer_Moore(text,pattern)
print(answer)