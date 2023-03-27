def isBabyGin(i,k):
    global answer
    if i == k:
        left, right = seq[:3],seq[3:]
        if (left[0]+2 == left[1]+1 == left[2]) or (left[0]==left[1]==left[2]):
            if (right[0]+2 == right[1]+1 == right[2]) or (right[0]==right[1]==right[2]):
                answer = True
                return
            return
        return
    
    for j in range(i,6):
        seq[i],seq[j] = seq[j],seq[i]
        isBabyGin(i+1,k)
        seq[i],seq[j] = seq[j],seq[i]

inputs =  ('124783','667767','054060','101123')
for seq in inputs:
    answer = False
    seq = list(map(int,seq))
    isBabyGin(0,6)
    print(answer)