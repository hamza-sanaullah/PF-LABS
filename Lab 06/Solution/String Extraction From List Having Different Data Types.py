def extract_strings(lst):
    result = []
    for item in lst:
        if isinstance(item, str):
            result.append(item)
        elif isinstance(item, (list, tuple, set)):
            result.extend(extract_strings(item))
    return result


mixed_list = ["hello", 123, [1, 2, 3], "world", (4, 5), {"a", "b"}, "python"]


string_list = extract_strings(mixed_list)

# Print the new list
print(string_list)

