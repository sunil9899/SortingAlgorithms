def shellSort(lst):
    gap = len(lst) // 2
    while gap > 0:
        for i in range(gap, len(lst), gap):
            pos = i
            while pos > 0:
                if lst[pos] < lst[pos-gap]:
                    lst[pos-gap], lst[pos] = lst[pos], lst[pos-gap]
                pos = pos - gap
        gap = gap // 2

l = [10,2,56,44,45,3,56,8,4,8,9,6]
shellSort(l)
print('Sorted List: ', l)
