def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        lower = i
        for j in range(i+1,n):
            if arr[j] < arr[lower]:
                lower = j
        arr[i],arr[lower] = arr[lower],arr[i]
    return arr

arr = [8,4,48,26,3]
print(selection_sort(arr))