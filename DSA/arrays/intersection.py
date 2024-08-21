# Intersectin :
set_a ={1,2,3}
set_b = {3,4,5}
intesetion = set_a &set_b
print(intesetion)

# from arrays

# List comprehension
arr_1 = [1,2,3]
arr_2 = [3,4,5]
intesetion_arr = [x for x in arr_1 if x in arr_2]
print(intesetion_arr)


# for Loop
arr_1 = [1,2,3]
arr_2 = [3,4,5]
for i in arr_1:
    if i in arr_2:
        print([i])
