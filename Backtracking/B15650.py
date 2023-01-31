'''
백준 15650 N과 M 2
방문처리는 필요X
-> 오름차순으로 필요하므로, 현재 탐색위치보다 나중 위치에서 탐색을 시작한ㄷ.
   그러므로 사용한 숫자를 또 사용하진 않는다.
'''
def NM2(N,M,k,path):
    if len(path) == M:
        print(*path)
        return
    
    for i in range(k,N+1):
        NM2(N,M,i+1,path+[i])

NM2(4,2,1,[])