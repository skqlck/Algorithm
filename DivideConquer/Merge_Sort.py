def merge(left, right):
    result = []

    lp = 0
    rp = 0

    while lp<len(left) and rp<len(right):
        if left[lp] < right[rp]:
            result.append(left[lp])
            lp += 1
        else:
            result.append(right[rp])
            rp += 1
    result.extend(left[lp:])
    result.extend(right[rp:])

    return result

def mergeSort(lst):
    if len(lst) == 1:
        return lst

    m = len(lst)//2
    left = lst[:m]
    right = lst[m:]

    left = mergeSort(left)
    right = mergeSort(right)
    return merge(left, right)

lst = [6,8,4,3,1,5,3,2,4,8]
print(mergeSort(lst))