def preorder(root):
    global cnt
    if root:
        cnt += 1
        preorder(tree[root][0])
        preorder(tree[root][1])

T = int(input())
for test_case in range(1,1+T):
    E,N = map(int,input().split())
    edges = list(map(int,input().split()))
    tree = [[0,0] for _ in range(E+2)]
    for idx in range(0,len(edges),2):
        p,s = edges[idx],edges[idx+1]
        if tree[p][0]:
            tree[p][1] = s
        else:
            tree[p][0] = s
    cnt = 0
    preorder(N)
    print(f"#{test_case} {cnt}")