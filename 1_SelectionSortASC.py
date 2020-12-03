'''
In Selection sort, we find the minimum value and get this index number.
Swap this minimum value to current pointed value.
'''

# 1st way
print('**********1st Way**********')
lst = [25,36,5,12,78,1,5,2,5,4]
print('Unordered List: ', lst)
lst.sort()
print('Ordered List: ', lst)
 
# 2nd way
print('**********2nd Way**********')
lst = [25,36,5,12,78,1,5,2,5,4]
print('Unordered List: ', lst)
output = []
for i in range(len(lst)):
    output.append(min(lst))
    lst.remove(min(lst))
print('Ordered List: ', output)

#3rd Way
print('**********3rd Way**********')
lst = [25,36,5,12,78,1,5,2,5,4]
print('Unordered List: ', lst)
for i in range(len(lst)):
    min_val = min(lst[i:])
    min_val_idx = lst.index(min_val, i)
    lst[i], lst[min_val_idx] = min_val, lst[i]
print('Ordered List: ', lst)

#4th Way
print('**********4th Way**********')
lst = eval(input('Enter List values seperated by commas to sort: '))
lst = list(lst)
print('Unordered List: ', lst)
for i in range(len(lst)):
    min_val = min(lst[i:])
    min_val_idx = lst.index(min_val, i)
    lst[i], lst[min_val_idx] = min_val, lst[i]
print('Ordered List: ', lst)
