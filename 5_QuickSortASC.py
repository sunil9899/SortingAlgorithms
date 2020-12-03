'''
This algorithm is work on three conditions which checks in each iterations.
It will work in three steps.
The conditions are:
    1. Left_Index <= Right_Index
    2. Left_Value <= Pivot
    3. Right_Value >= Pivot
'''

# Function for to get the correct position of pivot value / assuming that the
# pivot value is placed at left initially.

def pivotLOC(lst, first, last):
    pivot = lst[first]
    left = first+1
    right = last
    while True:
        while left <= right and lst[left] <= pivot:
            left += 1
        while left <= right and lst[right] >= pivot:
            right -= 1
        if left > right:
            break
        else:
            lst[left], lst[right] = lst[right], lst[left]
    lst[first], lst[right] = lst[right], lst[first]
    return right

def recursiveFunc(lst, first, last):
    if first < last:
        pvt = pivotLOC(lst, first, last)
        recursiveFunc(lst, first, pvt-1)
        recursiveFunc(lst, pvt+1, last)

l = [10,5,69,85,3,2,45,87,6,889,1002,56,89]
recursiveFunc(l, 0, len(l)-1)
print(l)
