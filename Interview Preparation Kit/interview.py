def merge(arr, left, mid, right):
    i = left
    j = mid + 1
    k = left

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            sorted_arr[k] = arr[i]
            i += 1
            k += 1
        else:
            sorted_arr[k] = arr[j]
            j += 1
            k += 1

    if i > mid:
        for l in range(j, right + 1):
            sorted_arr[k] = arr[l]
            k += 1
    else:
        for l in range(i, mid + 1):
            sorted_arr[k] = arr[l]
            k += 1

    for l in range(left, right + 1):
        arr[l] = sorted_arr[l]


def mergeSort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        mergeSort(arr, left, mid)
        mergeSort(arr, mid + 1, right)
        merge(arr, left, mid, right)


n = 9
arr = [2, 1, 3, 3, 1, 2, 5, 4, 1]

sorted_arr = [0] * n
mergeSort(arr, 0, n - 1)

print(sorted_arr)
