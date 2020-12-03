def insertionSort(lst):
    for i in range(1,len(lst)):
        for j in range(i-1,-1,-1):
            if lst[i] < lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
                i -= 1
            else:
                continue
l = [12,1,5,45,7,8,55,1,2,5,78,99,1,3,4,5,9,36,7,9]
print('Original List: ', l)
insertionSort(l)
print('Ordered List:', l)
