
# Rotate an Array

# input = [1,2,3,4,5]
# output = [4,5,1,2,3]

# Right Rotation Function==============================
def rotateArray(nums ,  k):
    n = len(nums)
    k = k % n # handle the case where k is greater than the length of the array
    return nums[-k:] + nums[:-k]
nums = [1,2,3,4,5]
k = 2
print(rotateArray(nums , k))



# Left Rotation Function===============================
def rotate_left(arr, k):
    k = k % len(arr)  # Ensure k is within the bounds of the list length
    return arr[k:] + arr[:k]

arr = [1, 2, 3, 4, 5]
rotated_arr = rotate_left(arr, 2)
print(rotated_arr)  # Output: [3, 4, 5, 1, 2]

