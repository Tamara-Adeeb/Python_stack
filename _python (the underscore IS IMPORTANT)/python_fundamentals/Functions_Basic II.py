#Countdown - Create a function that accepts a number as an input. 
# Return a new list that counts down by one, from the number (as the 0th element) 
# down to 0 (as the last element).
def Countdown(a):
    list = []
    for i in range(a, -1, -1):
        list.append(i)
    return list
Countdown(5)
print(Countdown(5))

#Print and Return - Create a function that will receive a list with two numbers. 
# Print the first value and return the second.
def printReturn(a):
    print(a[0])
    return a[1]
print(printReturn([1,2]))

#First Plus Length - Create a function that accepts a list and returns the sum 
# of the first value in the list plus the list's length.
def firstPlusLength(a):
    return a[0]+len(a)
print(firstPlusLength([1,2,3,4]))

#Values Greater than Second - Write a function that accepts a 
# list and creates a new list containing only the values from the 
# original list that are greater than its 2nd value. Print how many 
# values this is and then return the new list. If the list has less than 
# 2 elements, have the function return False

def values_greater_than_second(a):
    newList = []
    for i in range(len(a)):
        if a[i] > a[1]:
            newList.append(a[i])
    print(len(newList))
    if len(newList) < 2:
        return False
    else:
        return newList
z = values_greater_than_second([5,2,3,2,1,4])
print(z)

#This Length, That Value - Write a function that accepts two integers as parameters: 
# size and value. The function should create and return a list whose length is equal 
# to the given size, and whose values are all the given value.
def length_and_value(a,b):
    list = []
    for i in range(a):
        list.append(b)
    return list
z = length_and_value(4,7)
print(z)
