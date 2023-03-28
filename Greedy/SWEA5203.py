def BabyGin(arr):
    n = len(arr)
    # Triplet
    for element in arr:
        if element > 2:
            return True
    # Run    
    for i in range(n-2):
        if arr[i] and arr[i+1] and arr[i+2]:
            return True
        
    return False

T = int(input())
for test_case in range(1,1+T):
    pick = list(map(int,input().split()))
    player1,player2 = [0]*10,[0]*10
    for i in range(12):

        if i%2:
            player2[pick[i]] += 1
            if BabyGin(player2):
                print(f"#{test_case} 2")
                break
        else:
            player1[pick[i]] += 1
            if BabyGin(player1):
                print(f"#{test_case} 1")
                break
    else:
        print(f"#{test_case} 0")