def insertion(arr):
    for i in range(1,len(arr)):
        start = arr[i]
        j = i - 1
        while j >= 0 and start < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = start

    return arr

arr = [2,6,3,1,4]
print(insertion(arr))