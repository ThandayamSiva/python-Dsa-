# 7. Check if a list is palindrome: Write a function to check if a list is a palindrome.

# A palindrome is a word , phase , number , or suqueence of characters that reads the same forward
# and backward , ignoring spaces, punctuation, and capitalization.

# Word Palindromes: "madam," "racecar," "level"
# Phrase Palindromes: "A man, a plan, a canal, Panama!"
# Number Palindromes: 121, 12321, 1001

def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False
word = "madam"
print(palindrome(word))

# two pointers Approach

def palindromeTwopointers(words):
    left , right = 0 , len(words)-1
    while left < right:
        if words[left] != words[right]:
            return False
        left +=1
        right -=1
    return True
words = "racecar"
print(palindromeTwopointers(words))
\
# Using Stacks

def palindromeusingStaks(words):
    stack = []
    for char in words:
        stack.append(char)
        
    reversed = ''
    while stack:
        reversed+= stack.pop()
        
    return words == reversed
words = "level"
print(palindromeusingStaks(words))



