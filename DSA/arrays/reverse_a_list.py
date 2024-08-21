arr = [1,2,3,4,5,6,7,8,9,10]

# using revese()
arr.reverse()
print(arr)

# using loops

array = [1,2,3,4,5,6,7,8,9,10]
for i in range(len(array)-1 ,-1, -1): # (lenght od array,stoping index , jumping index)
    print(array[i], end=" ")
    
    
aray = [1,2,3,4,5,6,7,8,9,10]
i = len(aray) -1
while i >= 0:
    print(aray[i] ,end=" ")
    i-=1 # decrement
    
    
aray = [1,2,3,4,5,6,7,8,9,10]
i = 0
while i <= len(aray):
    print(aray[-i] ,end=" ")
    i+=1 # Increment


s = ["h" ,"e" , "l" ,"l" ,"o"]
reversed = []
for i in range(len(s)-1 ,-1,-1):
    print(reversed.append(s[i]))
    
print(reversed)


s = ["h" ,"e" , "l" ,"l" ,"o"]
stack = []
for char in s:
    stack.append(char)
reversed = []
while stack:
    reversed.append(stack.pop())
print(reversed)


s = ["h" ,"e" , "l" ,"l" ,"o"]
stack =[]
for char in s:
    stack.append(char)
reversed = ""
while stack:
    reversed += stack.pop()
print(reversed)


# LeetCode
s = ["h" ,"e" , "l" ,"l" ,"o"]
left , right = 0 ,len(s)-1
while left < right:
    s[left] , s[right] =s[right] , s[left]
    left +=1
    right-=1
print()


# Using two pointers  reverse an array
def rotateArray(arr):
    left  = 0
    right = len(arr)-1
    while left < right:
        arr[left] , arr[right] = arr[right] , arr[left]
        left +=1 # increment
        right -=1 # decrement
    return arr
arr = [1,2,3,4,5]
print(rotateArray(arr))
