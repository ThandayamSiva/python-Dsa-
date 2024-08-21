def MostFrequantElement(my_tuple):
    dic = {}
    for el in my_tuple:
        if el in dic:
            dic[el] += 1
        else:
            dic[el] = 1
            
    print(dic)
    
    most_frequant = None
    count = 0
    
    for k , v in dic.items():
        if v  > count:
            count = v
            most_frequant = k
    return most_frequant

my_tuple = (1,2,3,2,4,5 , 5, 5, 2 ,2)
print(MostFrequantElement(my_tuple))