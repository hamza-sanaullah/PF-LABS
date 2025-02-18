def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    searches = 0

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid, searches
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
        searches += 1

    return -1, searches

# Example usage
lst = [11, 12, 22, 25, 34, 64, 90]
print("Sorted list:", lst)
target_element = 22
index, num_searches = binary_search(lst, target_element)
if index != -1:
    print(f"Element {target_element} found at index {index}.")
else:
    print(f"Element {target_element} not found in the list.")
print("Total searches:", num_searches)
