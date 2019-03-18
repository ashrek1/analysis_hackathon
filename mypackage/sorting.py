def bubble_sort(items):
    '''Return array of items, sorted in ascending order'''
    index = len(items) - 1
    while index >= 0:
        for i in range(index):
            if items[i] > items[i + 1]:
                items[i], items[i + 1] = items[i + 1], items[i]
        index -= 1
    return items

def merge(list1, list2):
    '''Return array of items, sorted in ascending order'''
    sorted_list = []
    list1_idx = 0
    list2_idx = 0
    while list1_idx < len(list1) and list2_idx < len(list2):
        if list1[list1_idx] <= list2[list2_idx]:
            sorted_list.append(list1[list1_idx])
            list1_idx += 1
        else:
            sorted_list.append(list2[list2_idx])
            list2_idx += 1

    if list1:
        sorted_list.extend(list1[list1_idx:])
    if list2:
        sorted_list.extend(list2[list2_idx:])
    return sorted_list

def merge_sort(items):
    '''Splits an array of items, then sorts via a merge_sort'''
    if len(items) <= 1:
        return items

    mid = len(items) // 2
    list1 = items[:mid]
    list2 = items[mid:]

    list1 = merge_sort(list1)
    list2 = merge_sort(list2)
    return list(merge(list1,list2))

def quick_sort(items):
    '''Return array of items, sorted in ascending order'''
    smaller = []
    mid   = []
    bigger  = []

    if len(items) <= 1:
        return items
    else:
        pivot = items[0]
        for i in items:
            if i < pivot:
                smaller.append(i)
            elif i > pivot:
                bigger.append(i)
            else:
                mid.append(i)
    smaller = quick_sort(smaller)
    bigger = quick_sort(bigger)
    return smaller + mid + bigger
