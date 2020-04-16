def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        return quicksort([x for x in arr[1:] if x < arr[0]]) + \
               [arr[0]] + \
               quicksort([x for x in arr[1:] if x >= arr[0]])
