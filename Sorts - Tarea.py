def bubble_sort_reverse(arr):
    n = len(arr)
    for i in range(n-1, 0, -1):
        for j in range(n-1, n-1-i, -1):
            if arr[j] > arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]

arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort_reverse(arr)
print("Sorted array:", arr)


def insertion_sort_reverse(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key > arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

arr = [64, 34, 25, 12, 22, 11, 90]
insertion_sort_reverse(arr)
print("Sorted array:", arr)

def selection_sort_reverse(arr):
    n = len(arr)
    for i in range(n-1, 0, -1):
        max_idx = i
        for j in range(i-1, -1, -1):
            if arr[j] < arr[max_idx]:
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]

arr = [64, 34, 25, 12, 22, 11, 90]
selection_sort_reverse(arr)
print("Sorted array:", arr)


def merge_sort_reverse(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort_reverse(L)
        merge_sort_reverse(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] > R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

arr = [64, 34, 25, 12, 22, 11, 90]
merge_sort_reverse(arr)
print("Sorted array:", arr)
