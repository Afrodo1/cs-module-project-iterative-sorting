def linear_search(arr, target):
    # Your code here


    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    start = 0
    end = (len(arr)-1)
    switch = True
    while switch is True:
        middle = (end + start)//2
        if arr == []:
            return -1
        if arr[middle]== target:
            switch = False
            return middle
        else:
            if start == end and target != arr[middle]:
                return -1
            elif target < arr[middle]:
                end = middle
            else:
                start = middle + 1



a = [1,2,3,4,5,6,7,8,9]

print(binary_search(a,9))

# half_a = slice(0, len(a)//2)

# print(a[half_a])
