def linear_search(arr, target):
    # Your code here


    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    curr_index = len(arr)//2
    cut = arr
    if cut[curr_index] == target:
        return curr_index
    else:
        if cut[curr_index] > target:
            cut = cut[slice(0,len(cut)//2)]
            binary_search(cut,target)
        if cut[curr_index] < target:
            cut = cut[slice(curr_index,len(cut)-1)]
            binary_search(cut,target)
    # Your code here



a = [1,2,3,4,5,6,7,8,9]

print(binary_search(a,1))

# half_a = slice(0, len(a)//2)

# print(a[half_a])
