# 1. Merge two sorted lists: Write a function to merge two sorted lists into one sorted list.


# Using Extend  just Merge
def mergeTwoSordtedLists(array_1 , array_2):
    array_1.extend(array_2)
    return array_1
array_1 = [1,2,3,4,5]
array_2 = [6,7,8,9,10]
print(mergeTwoSordtedLists(array_1 , array_2))


# Loops

def mergeTwoSortedLists(list1 , list2):
    sorted_list = []
    i , j = 0, 0
    
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            sorted_list.append(list1[i])
            i+=1
        else:
            sorted_list.append(list2[j])
            i-=1
            
    while i < len(list1):
        sorted_list.append(list1[i])
        i+=1
    while j < len(list2):
        sorted_list.append(list2[i])
        i-=1
        
    return sorted_list

array_1 = [1,2,3,4,5]
array_2 = [6,7,8,9,10]

print(mergeTwoSordtedLists(array_1 , array_2))



## Using heapqnext ?
import heapq

def mergeTwoSortedlistUsingHeapq(ar1 , ar2):
    return list(heapq.merge(ar1 , ar2))

list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
print(mergeTwoSortedlistUsingHeapq(list1, list2))


# Using Sorting ofter Concatanating
def mergeTwoListConcatenate(list1, list2):
    comnined_list = list1 + list2
    comnined_list.sort()
    return comnined_list
    
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]    
print(mergeTwoListConcatenate(list1 , list2))
