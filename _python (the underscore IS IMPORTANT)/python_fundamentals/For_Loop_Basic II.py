#Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
def biggie_size(a):
    for i in range(len(a)):
        if a[i] > 0:
            a[i] = "big"
    return a
print(biggie_size([-1, 3, 5, -5]))

#Count Positives - Given a list of numbers, create a function to replace the last 
# value with the number of positive values. (Note that zero is not considered to be a positive number).
def count_positives(a):
    count = 0
    for i in range(len(a)):
        if a[i] > 0:
            count += 1
    a[len(a)-1] = count
    return a
print(count_positives([-1,1,1,1]))

#Sum Total - Create a function that takes a list and returns the sum of all the values in the list.
def sum_total(a):
    sum = 0
    for i in range(len(a)):
        sum += a[i]
    return sum
print(sum_total([1,2,3,4]))

#Average - Create a function that takes a list and returns the average of all the values.x
def average(a):
    sum = 0
    for i in range(len(a)):
        sum += a[i]
    return sum/len(a)
print(average([1,2,3,4]))

#Length - Create a function that takes a list and returns the length of the list.
def length(a):
    return len(a)
def length1(a):
    count = 0
    for i in a:
        count += 1
    return count
print(length([37,2,1,-9]))
print(length1([37,2,1,-9]))

#Minimum - Create a function that takes a list of numbers and returns the minimum 
# value in the list. If the list is empty, have the function return False.
def minimum(a):
    min = a[0]
    if len(a) == 0:
        return False
    for i in range(len(a)):
        if min > a[i]:
            min = a[i]
    return min
print(minimum([37,2,1,-9]))

#Maximum - Create a function that takes a list and returns the maximum value in the list. 
# If the list is empty, have the function return False.
def maximum(a):
    max = a[0]
    if len(a) == 0:
        return False
    for i in range(len(a)):
        if max <  a[i]:
            max = a[i]
    return max
print(maximum([37,2,1,-9]))

#Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, 
# average, minimum, maximum and length of the list.
Example: ultimate_analysis([37,2,1,-9]) should 
return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }
def ultimate_analysis(a):
    sum = 0
    min = a[0]
    max = a[0]
    dir = {}
    for i in range(len(a)):
        sum += a[i]
        if max < a[i]:
            max = a[i]
        if min > a[i]:
            min = a[i]
    avr = sum/len(a)
    dir["sumTotal"] = sum
    dir["average"] = avr
    dir["minimum"] = min
    dir["maximum"] = max
    dir["length"] = len(a)
    return dir
print(ultimate_analysis([37,2,1,-9]))

#Reverse List - Create a function that takes a list and return that list with values reversed. 
# Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]





