# 1st way
print('**********1st Way**********')
lst = [25,36,5,12,78,1,5,2,5,4]
print('Unordered List: ', lst)
lst.sort(reverse=True)
print('Ordered List: ', lst)

# 2nd way
print('**********2nd Way**********')
lst = [25,36,5,12,78,1,5,2,5,4]
print('Unordered List: ', lst)
for i in range(len(lst)):
    max_value = max(lst[i:])
    max_value_idx = lst.index(max_value, i)
    lst[i], lst[max_value_idx] = max_value, lst[i]
print('Ordered List: ', lst)

# 3rd way
print('**********3rd Way**********')
lst = [25,36,5,12,78,1,5,2,5,4]
print('Unordered List: ', lst)
output = []
for _ in range(len(lst)):
    output.append(max(lst))
    lst.remove(max(lst))
print('Ordered List: ', output)
