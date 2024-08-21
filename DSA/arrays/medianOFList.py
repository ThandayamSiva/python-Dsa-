#2. Find the median of a list: Write a function to find the median of a list.

# approach

# 1. Sort the list :The median is defined as the middel value when the data is ordered:
# therefore , sorting the list is a crucial step

# 2. Find the median:

# Note :
#       -> if the list has an Odd Number of elements , the median is the middle element
#       -> if the list has an even numbers of elements , the median is the average of two middle elements:


def find_median(lst):
    # Sort the list
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    
    # Check if the list length is odd or even
    if n % 2 == 1:
        # Odd length: median is the middle element
        median = sorted_lst[n // 2]
    else:
        # Even length: median is the average of the two middle elements
        mid1, mid2 = sorted_lst[n // 2 - 1], sorted_lst[n // 2]
        median = (mid1 + mid2) / 2
    
    return median

# Example usage
print(find_median([1, 3, 5, 7, 9]))  # Output: 5 (odd number of elements)
print(find_median([1, 2, 3, 4, 5, 6]))  # Output: 3.5 (even number of elements)


        