def hoare(l,r):
    p = l
    lp = l
    rp = r
    while lp<=rp:
        while lp<=rp and lst[lp] <= lst[p]:
            lp += 1
        while lp<=rp and lst[rp] >= lst[p]:
            rp -= 1
        if lp < rp:
            lst[lp], lst[rp] = lst[rp], lst[lp]
    lst[p], lst[rp] = lst[rp], lst[p]

    return rp

def lomuto(l,r):
    p = r
    i = l-1
    for j in  range(l,r):
        if lst[j] < lst[p]:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    i += 1
    lst[i], lst[p] = lst[p], lst[i]

    return i

def quicks(l,r):
    if l < r:
        p = lomuto(l, r)
        quicks(l,p-1)
        quicks(p+1,r)

lst = [3,2,4,6,9,1,8,7,5]
quicks(0,len(lst)-1)
print(lst)