# T = int(input())
# for test_case in range(1,1+T):
#     N = int(input())
#     pascal = [[1],[1,1]]
#     for i in range(N-2):
#         new_line = [1]
#         for j in range(len(pascal[-1])-1):
#             new_line.append(pascal[-1][j]+pascal[-1][j+1])
#         new_line.append(1)
#         pascal.append(new_line)
#
#     print(f"#{test_case}")
#     for i in range(N):
#         print(*pascal[i])

T = int(input())
for test_case in range(1,1+T):
    N = int(input())
    pascal = [[1],[1,1]]
    for i in range(N-2):
        new_line = []
        stack = pascal[-1][:]
        while stack:
            if new_line:
                new = stack.pop()
                new_line.append(before+new)
                before = new
            else:
                before = stack.pop()
                new_line.append(before)
        new_line.append(1)
        pascal.append(new_line)
    print(f"#{test_case}")
    for i in range(N):
        print(*pascal[i])