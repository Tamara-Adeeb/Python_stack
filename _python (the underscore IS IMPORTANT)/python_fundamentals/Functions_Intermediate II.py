x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# #Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x[1][0] = 15
print(x)
#Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]["last_name"] = "Bryant"
print(students)
#In the sports_directory, change 'Messi' to 'Andres'
sports_directory["soccer"][0] = "Andres"
print(sports_directory)
#Change the value 20 in z to 30
z[0]["y"] = 30
print(z)

#Iterate Through a List of Dictionaries
def iterateDictionary(dict): #dict represent dictionarie
    for i in dict:
        for key , val in i.items():
            print(f"{key} - {val}", end=", ")
        print("")
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
# iterateDictionary(students) 
#Get Values From a List of Dictionaries
def iterateDictionary2(key_name, list_of_dict):
    for student in list_of_dict:
        print(student[key_name])
iterateDictionary2("last_name", students)

#Iterate Through a Dictionary with List Values
def printInfo(l_dict):#l_dict is dictionary where the key value is list
    for key in l_dict:
        print(len(l_dict[key]),key.upper())
        for i in l_dict[key]:
            print(i)
        print("")
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)
