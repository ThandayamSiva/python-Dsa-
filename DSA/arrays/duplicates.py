# Remove Duplicates:

# linear Search / brute-force approach
# 1. iterate through each element of the array.
# 2. Check for uniques : for each element , check whether it is already exits in unique ?
arr  = [1,2,3,4,3,2,15,6,7,2,9]
duplicates = []
unique = []
for i in arr:
    if i in unique:
        duplicates.append(i)
    else:
        unique.append(i)
print(duplicates)
print(unique)


# Using set() datatypes:
arr  = [1,2,3,4,3,2,15,6,7,2,9]
duplicate_removed = set(arr)
print(duplicate_removed)


arr  = [1,2,3,4,3,2,15,6,7,2,9]
unique = set()
for j in arr:
    if j not in unique:
        unique.add(j)
print(unique)

# normal way:
arr  = [1,2,3,4,3,2,15,6,7,2,9]
unique = []
for j in arr:
    if j not in unique:
        unique.append(j)
print(unique)
        

# Using Hash:
def sortingUsinghash(arr):
    dic = {}
    for i in arr:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    print(dic)
    unique = []
    for k , v in dic.items():
        if v == 1:
            unique.append(k)
    return unique
arr  = [1,2,3,4,3,2,15,6,7,2,9]
print(sortingUsinghash(arr))


