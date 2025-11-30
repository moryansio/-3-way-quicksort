def quicksort_3way(arr):

    if len(arr) <= 1:
        return arr
    lt, eq, gt = [], [], []
    pivot = arr[len(arr) // 2]
    for x in arr:
        if x < pivot:
            lt.append(x)
        elif x > pivot:
            gt.append(x)
        else:
            eq.append(x)
    return quicksort_3way(lt) + eq + quicksort_3way(gt)