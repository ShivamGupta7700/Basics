# import json

#More about the dictionary

Employees = {}
print('Empty' if Employees else "Ok")

Employees = dict([['name', 'Shivam'],['net worth', '2 billion dollars']])
print(Employees)


Employees = dict(zip(('name', 'net worth', 'age'),('Shivam Gupta', '2 billion dollar','17')))
print(Employees)


#Observation

# ClassMarks = {}
# n = int(input('How many student >> '))
# for a in range(n):
#     rollNo , Marks = eval(input('Enter your Roll no. , Marks . '))


# Better method 

dictionary = {}

# n = int(input('Enter ther total number of the student >>>> '))
# for student in range(n):
#         Rn , M = map(int, input('Enter the (RollNo) | then (Marks)').split()) # We can use eval(input('Enter the rn | marks >> '))
#         dictionary[Rn] = M
# print(dictionary)


# Now fromkeys() function
Default = 500


newDictionary = dict.fromkeys([1,2,3,4,5], Default)
print(newDictionary)


#Now we use setdefault() function

d = {1:100,2:200,3:300,4:400}
d.setdefault(5,500)
print(d) #{1: 100, 2: 200, 3: 300, 4: 400, 5: 500}
d.setdefault(6)
print(d) #{1: 100, 2: 200, 3: 300, 4: 400, 5: 500, 6: None}


print(d.setdefault(5, 600)) # it willchange nothing and it return the already existing value of the key given

#update function is in  the othe file already studied


# pop() function

Cars = {
    "Name":"Rolls Royce",
    "Price(cr)": 7,
    "info":{
        "engine":"6850cc",
        "Seats":5
    }
}


print(Cars.pop(2, 'not found'))

#Using the popitem() function

Cars.popitem() #removes items from the last 
print(Cars)
