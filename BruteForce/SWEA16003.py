"""
찾는 순서를 오름차순으로 한다면 나오는 것들이 오름차순으로 나온다.
스트링을 가지고 하는 것이 아니라 완전탐색으로 하나씩 찾아가야한다!
"""
def numbering(number):
    global answer
    if len(answer) == limit:
        return
    if number <= N:
        answer.append(str(number)+".png")

    for i in range(10):
        if int(str(number)+str(i)) <= N:
            numbering(int(str(number)+str(i)))

T = int(input())
for test_case in range(1,1+T):
    answer = []
    N = int(input())
    limit = min(50,N)
    for i in range(1,10):
        if len(answer) < limit:
            numbering(i)
    print(f"#{test_case}",*answer)