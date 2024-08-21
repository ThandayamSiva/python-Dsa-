# find Even Numbers

## Using List Comprehension
arr = [1,2,3,4,5,6,7,8,9,10]
even = [x for x in arr if x%2 == 0]
print(even)


arr = [1,2,3,4,5,6,7,8,9,10]
for i in arr:
    if i % 2 == 0:
        print(i , end=" ")
        
  
    
print()
# Even and Odd print

def findEvenOdd(arr):
    even = []
    odd = []
    for i in arr:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    print(even)
    print(odd)
arr = [1,2,3,4,5,6,7,8,9,10]
findEvenOdd(arr)


## Using Stack
def findEvenOddUsingStack(arr):
    stack = []
    ev = []
    od = []
    for el in arr:
        stack.append(el)
        if stack[-1] % 2 == 0:
            ev.append(stack[-1])
        else:
            popped = stack.pop()
            od.append(popped)
            
    print(ev)
    print(od)
arr = [1,2,3,4,5,6,7,8,9,10]
findEvenOddUsingStack(arr)



## Using While Loop
arr = [1,2,3,4,5,6,7,8,9,10]
i = 0
evens = []
while i < len(arr):
    if arr[i] % 2 == 0:
        evens.append(arr[i])
    i+=1
print(evens)


