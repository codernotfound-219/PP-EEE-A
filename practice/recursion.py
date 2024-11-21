
def prime_factors(num, fact=2):
    if num==0 or num==1:
        return
    elif num%fact == 0:
        print(fact, end=" ")
        prime_factors(num//fact, fact)
    else:
        prime_factors(num, fact+1)

prime_factors(48)

def merge(array, l, m, r):
    n1 = m-l+1
    n2 = r-m

    L = [0]*n1
    R = [0]*n1

    for i in range(n1):
        L[i] = array[i+l]

    for i in range(n2):
        R[i] = arr[m+i+1]

    i = j = 0
    k = l

    while (i < n1 and j < n2):
        if L[i] > R[j]:
            array[k] = R[j]
            j += 1
        else:
            array[k] = L[i]
            i += 1
        k+=1

    while (i < n1):
        array[k] = L[i]
        i += 1
        k += 1

    while (j < n2):
        array[k] = R[j]
        j += 1
        k += 1

def mergeSort(arr, l, r):
    if (l >= r):
        return
    
    mid = l + (r-l)//2
    mergeSort(arr, l, mid)
    mergeSort(arr, mid+1, r)
    merge(arr, l, mid, r)

arr = [6, 2, 2, 31, 45,32, 521 , 24, 2]
mergeSort(arr, 0, len(arr)-1)
print()
for i in arr:
    print(i, end = " ")
