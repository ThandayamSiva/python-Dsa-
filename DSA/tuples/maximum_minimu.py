# find maximum and minimum


def findMAxMin(my_tuple):
    return max(my_tuple) , min(my_tuple)
my_tuple = (1,2,3,4 ,10)
print(findMAxMin(my_tuple))

def findLaregetsSmallest(myTuple):
    largest  = my_tuple[0]
    smallest = my_tuple[0]
    for el in myTuple:
        if el > largest:
            largest = el
        else:
            if el < smallest:
                smallest = el
    print(largest)
    print(smallest)
my_tuple = (1,2,3,4 ,10)
findLaregetsSmallest(my_tuple)