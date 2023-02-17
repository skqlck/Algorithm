import sys
sys.stdin = open("input.txt","r")
def baseball(hitters):
    score = 0
    hit_idx = 0
    for inning in innings:
        out = 0
        base = [0,0,0,0]
        while out < 3:
            if inning[hitters[hit_idx]] == 0:
                out += 1
            elif inning[hitters[hit_idx]] == 1:
                score += base[3]
                base[1],base[2],base[3] = 1,base[1],base[2]
            elif inning[hitters[hit_idx]] == 2:
                score += (base[2]+base[3])
                base[1],base[2],base[3] = 0,1,base[1]
            elif inning[hitters[hit_idx]] == 3:
                score += (base[1]+base[2]+base[3])
                base[1],base[2],base[3] = 0,0,1
            else:
                score += 1+sum(base)
                base = [0,0,0,0]
            hit_idx = (hit_idx+1)%9
    return score

def make_entry(entry):
    global answer
    if len(entry) == 8:
        answer = max(answer,baseball(entry[:3]+[0]+entry[3:]))
        return
    for i in range(1,9):
        if not visited[i]:
            entry.append(i)
            visited[i] = 1
            make_entry(entry)
            visited[i] = 0
            entry.pop()


N = int(input())
innings = [list(map(int, input().split())) for _ in range(N)]
answer = 0
visited = [0]*9
make_entry([])
print(answer)