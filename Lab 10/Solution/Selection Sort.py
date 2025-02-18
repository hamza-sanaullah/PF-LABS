def selection_sort(arr):
    n = len(arr)
    swaps = 0
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        swaps += 1
        print(f"Iteration {i + 1}: {arr}")
    return arr, swaps

# Example usage
lst = [64, 34, 25, 12, 22, 11, 90]
print("Original list:", lst)
sorted_lst, num_swaps = selection_sort(lst)
print("Sorted list:", sorted_lst)
print("Total swaps:", num_swaps)
