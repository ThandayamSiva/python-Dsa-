# 8. Find the first duplicate: Write a function to find the first duplicate element in a list.

# input = [1,2,3,4,2,5]
# output = 2

def FirstDuplicateNumbers(nums):
    unique = set()
    for el in nums:
        if el not in unique:
            unique.add(el)
        else:
            print(el)
            break
nums =[21, 22, 23, 24, 25, 22, 26, 27, 21]
FirstDuplicateNumbers(nums)


def firstDuplicateNumbers(nums):
    data = []
    for el in nums:
        if el not in data:
            data.append(el)
        else:
            print(el)
            break
nums = [21, 22, 23, 24, 25, 22, 26, 27, 21]
firstDuplicateNumbers(nums)    

   