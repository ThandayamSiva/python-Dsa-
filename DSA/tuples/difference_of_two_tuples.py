# to find elements in the first tuple that are not in the second, then convert back to a tuple.

my_tuple1 = (1,2,3,4)
my_tuple2 = (1,2,3)
difference  = set(my_tuple1).difference(set(my_tuple2))
print(difference)




