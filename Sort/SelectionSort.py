def selectionSort(array):
    N = len(array)
    for i in range(N-1):
        minIdx = i
        for j in range(i+1,N):
            if array[minIdx] > array[j]:
                minIdx = j
        array[i],array[minIdx] = array[minIdx],array[i]

    return array

array = list(map(int,input().split()))
print(selectionSort(array))
