#Lambda, Python Built in Functions(map(),),Sequences

def myfunc(a, b):
    z = []
    for i in range(len(a)):
        z.append(f"{a[i]} {b[i]}")
    return z

x= myfunc(('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))
print(x)

#make the above in one line code
#The map() function executes a specified function for each item in an iterable. 
# The item is sent to the function as a parameter.

print(list(map(lambda a,b:f"{a} {b}",('apple', 'banana', 'cherry'),('orange', 'lemon', 'pineapple') )))

#In this lesson, you’ll see some of the problems you could run into if you use mutable data structures to 
# store your data set. Then, you’ll see how you can approach this data set with immutable data sctrutures.

#You’ll learn how you can use .namedtuple() from the collections module, which is built into Python, 
# in order to represent your data in an immutable data structure so it can’t be modified in-place.

#it is like class and instance(object) but immutable data structure so it can’t be modified in-place.

