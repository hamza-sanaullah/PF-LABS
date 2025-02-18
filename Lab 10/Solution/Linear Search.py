def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i


# Example usage
lst = [64, 34, 25, 12, 22, 11, 90]
print("Original list:", lst)
target_element = 22
index = linear_search(lst, target_element)
if index != -1:
    print(f"Element {target_element} found at index {index}.")
else:
    print(f"Element {target_element} not found in the list.")
