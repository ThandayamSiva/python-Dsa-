# Using Set

my_tuple = (1,2,3,4,5,1,2,3)
unique = set(my_tuple)
print(unique)

# List Compreshension with seen Set 

my_tuple = (1,2,3,4,5,1,2,3)
seen = set()
new_list = tuple(x for x in my_tuple if x not in seen and not seen.add(x))
print(new_list)