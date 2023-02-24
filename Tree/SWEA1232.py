def cal(num1,num2,exp):
    if exp == "+":
        return num1+num2
    if exp == "-":
        return num1-num2
    if exp == "*":
        return num1*num2
    if exp == "/":
        return num1/num2
def postOrder(start):
    global stack
    if start:
        postOrder(children[start][0])
        postOrder(children[start][1])
        if type(tree[start]) == int:
            stack.append(tree[start])
        else:
            a = stack.pop()
            b = stack.pop()
            stack.append(cal(b,a,tree[start]))

for test_case in range(1,11):
    N = int(input())
    children = [[0,0] for _ in range(N+1)]
    tree = [0]*(N+1)
    for _ in range(N):
        line = input().split()
        if len(line) == 4:
            node,value,left,right = line
            node,left,right = int(node),int(left),int(right)
            tree[node] = value
            children[node][0] = left
            children[node][1] = right
        elif len(line) == 2:
            node,value = map(int,line)
            tree[node] = value
    stack = []
    postOrder(1)
    print(f"#{test_case} {int(stack[0])}")