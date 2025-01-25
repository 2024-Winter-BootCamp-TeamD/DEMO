def merge_lists_unique(list_a, list_b):
    merged = list_a[:]
    for item in list_b:
        if item not in merged:
            merged.append(item)
    return merged

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
merged_result = merge_lists_unique(list1, list2)
print("Merged Unique List:", merged_result)