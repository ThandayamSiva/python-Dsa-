#3. Find the most frequent element: Write a function to find the most frequent element in a list.


def findMostFrequant(arr):
    dic = dict()
    for el in arr:
        if el in dic:
            dic[el]+=1
        else:
            dic[el]=1
    
    print(dict)
    most_frequant = None
    max_count = 0
    for k , v in dic.items():
        if v > max_count:
            max_count = v
            most_frequant = k
    print(most_frequant)
        
arr  = [1, 3, 1, 2, 1, 4, 2]
findMostFrequant(arr)
