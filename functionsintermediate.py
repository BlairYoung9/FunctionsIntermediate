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

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

#1
x[1][0]=15
print(x)

students[0]['last_name'] = "Bryant"
print(students)

sports_directory['soccer'][0] = "Andres"
print(sports_directory)

z[0]['y']=30
print(z)

#2
def iterateDictionary(some_list):
    for count in range(0, len(some_list)):
        print("first name:", some_list[count]['first_name'])
        print("last name: ", some_list[count]['last_name'])

iterateDictionary(students)

#3
def iterateDictionary2(key_name, some_list):
    for count in range(0, len(some_list)):
        if key_name == 'first_name':
            print(some_list[count]['first_name'])
        elif key_name == 'last_name':
            print(some_list[count]['last_name'])
            
iterateDictionary2('first_name', students)

#4
def print_info(some_dict):
    for key in some_dict:
        print(len(some_dict[key]), key.upper())
        for item in some_dict[key]:
            print(item)

print_info(dojo)

