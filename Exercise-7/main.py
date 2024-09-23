def reverse_list(lst):
    return lst[::-1]

def concatenate_lists_index_wise(lst1, lst2):
    return [i + j for i, j in zip(lst1, lst2)]

def square_list_items(lst):
    return [i**2 for i in lst]

def concatenate_lists_sorted(lst1, lst2):
    return sorted(lst1 + lst2)

def iterate_both_lists_simultaneously(lst1, lst2):
    return [(i, j) for i, j in zip(lst1, lst2)]

def remove_empty_strings(lst):
    return [i for i in lst if i]

def add_item_after_specified(lst, item, new_item):
    index = lst.index(item) + 1
    return lst[:index] + [new_item] + lst[index:]

def extend_nested_list(lst, sublist):
    lst.extend(sublist)
    return lst

def replace_list_item(lst, item, new_item):
    return [new_item if i == item else i for i in lst]

def remove_all_occurrences(lst, item):
    return [i for i in lst if i != item]

# Predefined values for testing the exercises
lst1 = [1, 2, 3, 4, 5]
lst2 = [6, 7, 8, 9, 10]
str_lst = ["apple", "", "banana", " ", "cherry", ""]
sublist = [11, 12, 13]
item = 3
new_item = 99
replace_item = 2
replace_with = 88
remove_item = 1

print("1. Reverse List:", reverse_list(lst1))
print("2. Concatenate two lists index-wise:", concatenate_lists_index_wise(lst1, lst2))
print("3. Square every item in the list:", square_list_items(lst1))
print("4. Concatenate two lists (sorted):", concatenate_lists_sorted(lst1, lst2))
print("5. Iterate both lists simultaneously:", iterate_both_lists_simultaneously(lst1, lst2))
print("6. Remove empty strings:", remove_empty_strings(str_lst))
print("7. Add new item after specified:", add_item_after_specified(lst1, item, new_item))
print("8. Extend nested list:", extend_nested_list(lst1, sublist))
print("9. Replace list's item with new value:", replace_list_item(lst1, replace_item, replace_with))
print("10. Remove all occurrences of item:", remove_all_occurrences(lst1, remove_item))

