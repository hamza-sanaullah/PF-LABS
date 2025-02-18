def insertion_sort(arr):
    n = len(arr)
    swaps = 0
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            swaps += 1
        arr[j + 1] = key
        print(f"Iteration {i}: {arr}")
    return arr, swaps

# Example usage
lst = [64, 34, 25, 12, 22, 11, 90]
print("Original list:", lst)
sorted_lst, num_swaps = insertion_sort(lst)
print("Sorted list:", sorted_lst)
print("Total swaps:", num_swaps)
