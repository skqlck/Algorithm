def quicksort(A):
    n = len(A)
    if n < 2:
        return A
    elif n == 2:
        a,b = A
        if a<b:
            return [a,b]
        return[b,a]
    else:
        left,middle,right = [],[],[]
        pivot = A[len(A)//2]
        for element in A:
            if element > pivot:
                right.append(element)
            elif element == pivot:
                middle.append(element)
            else:
                left.append(element)
        return quicksort(left) + middle + quicksort(right)

A = [5,3,2,3,4,1,5,5,3,3,2,4,15,3,2,1,5,4,8,6,3,1,2,3,4,8,6,5,7,9]
print(quicksort(A))