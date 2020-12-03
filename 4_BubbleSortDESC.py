# 1st way
print('**********1st Way**********')
lst = [25,36,5,12,78,1,5,2,5,4]
print('Unordered List: ', lst)
for _ in range(len(lst)):
    for i in range(len(lst)-1):
        if lst[i] < lst[i+1]:
            lst[i],lst[i+1] = lst[i+1], lst[i]
print('Ordered List: ', lst)

# 2nd way
print('**********2nd Way**********')
lst = [25,36,5,12,78,1,5,2,5,4]
print('Unordered List: ', lst)
for _ in range(len(lst),1,-1):
    for i in range(_-1):
        if lst[i] < lst[i+1]:
            lst[i],lst[i+1] = lst[i+1], lst[i]
            print(lst)
        print(lst)
    print()
print('Ordered List: ', lst)
