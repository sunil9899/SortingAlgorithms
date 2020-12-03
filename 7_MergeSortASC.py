import time
def MergeSort(lst):
    if len(lst) > 1:
        mid = len(lst) // 2
        left_list = lst[:mid]
        right_list = lst[mid:]
        MergeSort(left_list)
        MergeSort(right_list)
        i=0
        j=0
        k=0
        while i<len(left_list) and j<len(right_list):
            if left_list[i]<right_list[j]:
                lst[k] = left_list[i]
                i += 1
                k += 1
            else:
                lst[k] = right_list[j]
                j += 1
                k += 1
        while i<len(left_list):
            lst[k] = left_list[i]
            i += 1
            k += 1
        while j<len(right_list):
            lst[k] = right_list[j]
            j += 1
            k += 1

l = [12,56,985,6,5,42,3,78]
print('Original List: ', l)
MergeSort(l)
print(l)
