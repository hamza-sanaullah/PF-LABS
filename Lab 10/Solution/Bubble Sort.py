def bubble_sort(arr):
    n = len(arr)
    swaps = 0
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

                swaps += 1
        print(f"Iteration {i + 1}: {arr}")
    return arr, swaps

# Example usage
lst = [64, 34, 25, 12, 22, 11, 90]
print("Original list:", lst)
sorted_lst, num_swaps = bubble_sort(lst)
print("Sorted list:", sorted_lst)
print("Total swaps:", num_swaps)
