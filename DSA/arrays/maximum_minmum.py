# Find Maximum:

arr = [1,2,3,4,5,6,7,8,9]
largest = arr[0] # 2=3
for i in arr:  # 1 , 2 , 3 , 4
    if i > largest:  # 1 >1 f, 2 >1 T, 3 >2 T, 4>3 T
        largest = i
print(largest)


# Find Minimum in array

array = [ 1,2,3,4,5,6,7]
smallest = array[0]
for i in array:
    if i < smallest:
        smallest = i
print(smallest)


# Input: nums = [4, 2, 5, 1, 6, 3]
# Output: [6, 1]
# Explanation: The maximum element is 6, and the minimum element is 1.

nums = [1, 5, 7, 2, 9, 3]
largest = nums[0]
smallest = nums[0]
for el in nums:
    if el > largest:
        largest = el
    if el < smallest:
        smallest = el
print([largest , smallest])



# Two-pointer technique

def TwoSum(nums , target):
    left = 0
    right = len(nums)-1
    
    while left < right:
        sum_of = nums[left] + nums[right]
        if sum_of == target:
            return nums[left] , nums[right]
        if sum_of < target:
            left +=1
        else:
            right-=1
    return None
    
nums = [2,7,11,15]
target = 9
print(TwoSum(nums , target))
            
    
            