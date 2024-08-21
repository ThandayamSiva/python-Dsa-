
# Using sort built in function 
arr = [2,6,1,3,10,4,7,5,8,9] # original array updated.
arr.sort()
print(arr)

# Using Soring() built in function
array = [2,6,1,3,10,4,7,5,8,9]
modified_arr = sorted(array)
print("oiginal Array",array) 
print("Modified Array",modified_arr)


# Using : 
# Compares a current element with all subsequent elements and swaps if a smaller one is found.
def SortedArray(nums):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] > nums[j]:
                nums[i] , nums[j] = nums[j] , nums[i]
    return nums
    
nums = [2,6,1,3,10,4,7,5,8,9]
print(SortedArray(nums))



 
#BUbble Sort :
#Swaps adjacent elements and continues until no swaps are needed.
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Flag to check if any swap happened in this pass
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # If no swaps occurred, the array is sorted
        if not swapped:
            break
    return arr

# Example usage
array = [64, 25, 12, 22, 11]
sorted_array = bubble_sort(array)
print("Sorted array:", sorted_array)
