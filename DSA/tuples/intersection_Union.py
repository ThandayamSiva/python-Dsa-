# Inersection

# convert tuples into set
my_tuple1 = (1,2,3)
my_tuple2 = (1,2,4)
inersection = set(my_tuple1).intersection(set(my_tuple2))
print(inersection)


my_tuple1 = (1,2,3)
my_tuple2 = (1,2,4)
inersection = set(my_tuple1) & (set(my_tuple2))
print(inersection)

# Union 

# convert back into tuple

my_tuple1 = (1,2,3)
my_tuple2 = (1,2,4)
union = set(my_tuple1).union((set(my_tuple2)))
print(tuple(union))


my_tuple1 = (1,2,3)
my_tuple2 = (1,2,4)
union = set(my_tuple1) | (set(my_tuple2))
print(tuple(union))


# List Comprehension
my_tuple1 = (1,2,3)
my_tuple2 = (1,2,4)
intersection = tuple(x for x in my_tuple1 if x in my_tuple2)
print(inersection)

my_tuple1 = (1,2,3)
my_tuple2 = (1,2,4)
union = tuple(set(x for x in my_tuple1 + my_tuple2))
print(union)

