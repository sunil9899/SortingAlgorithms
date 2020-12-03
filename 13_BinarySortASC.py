# In binary search we have a list and we have to find a key that is available in the list or not?

def binarySearch(lst, key):
    lst.sort()
    low = 0
    high = len(lst)-1
    status = False
    idx = 0
    while low <= high and not status:
        mid = (low+high)//2
        if key == lst[mid]:
            status = True
            idx = mid
        elif key > lst[mid]:
            low = mid+1
        else:
            high = mid-1
    if status == True:
        print(f'Key is found at Index= {idx}')
    else:
        print('Key is not found')

l = [12,5,65,9,8,45,4,546,56,56456,45,546,2,4,5]
print('Entered List: ', l)
k = int(input('Enter Key value to search: '))
binarySearch(l, k)
print('Entered Soretd List: ', l)
