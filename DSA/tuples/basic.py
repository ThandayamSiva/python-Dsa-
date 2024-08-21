# 1. What is a tuple in Python?
# 2. How do you create a tuple?
# 3. How do you access elements in a tuple?
# 4. Can you modify a tuple? Why or why not?
# 5. How do you compare tuples?

# 1. A tuple in python is an immutable , ordered collection of elements .
# Once a tuple is crated , you canot modify its contents , meaning you can't add , remove , or change elements within the tuple

# 2. create a tuple by placing elements inside parantheses () and separating them with commas.

my_tuple = (1, "Siva" , ["namathe"])
print(type(my_tuple))


# 3.  access element Using index , which start at 0.

my_tuple = (1,2,3,4,5,6)
access = my_tuple[3]
print(access)

# 4. we cannat modifid tuple but we have another way to modified tuple using list

my_tuple = (1,2,3,4,5,6)
change = list(my_tuple)
change[3]=6
print(change)


# 5. Tuples are compared elements b elements , starting from the first element . if the first element are euqal , the next elements are compared , and so  on
# (1,2,3) <  (1,2,4) because 3 is lless than 4