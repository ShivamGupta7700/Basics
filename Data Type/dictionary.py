# Dictionary are use to store data values in key:value pairs
# They are mutable data type & Don't allow duplicate key

dictionary = {
    "Name":"Shivam",# Key : Value
    "Age":16,
    "isAdult":False,
    "Class":11,
    "ProgrammingLanguage":["Python","Javascript"] #value can have any data type tuple/list any
}

# There is no order in dictionary / index

#// ACCESSING VALUE
print(dictionary["Name"])

#//Introducing new key:value
dictionary["RollNo"] = 44

print(dictionary)

# Nested dictionary

Cars = {
    "Name":"Rolls Royce",
    "Price(cr)": 7,
    "info":{
        "engine":"6850cc",
        "Seats":5
    }
}

print(Cars["info"]["Seats"])


# Methods
print(Cars.keys()) #Don't return nesting dictionary
print(list(Cars.keys()))



print(Cars.values())
print(list(Cars.values()))


#.items()

print(Cars.items())

#.get()
print(Cars.get("info"))
print(Cars.get("Launched")) # this will return none not an error like Cars["keyadsda"]

Cars.update({"Launched":"I don't Know"})#Updating dictionary
print(Cars)