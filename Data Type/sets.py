#collection of unordered items
#each element must be unique
#it is MUTABLE 

#it can store only immutable data type ELEMENT

cars = {"Rolls Royce","BMW M4", 7, 1.54}
print(cars)
print(type(cars))

numbers = {1,3,323,23,3,33,3}
print(numbers)#Ignore Duplicate Values

print(len(numbers))

Empty_Set = set()
print(type(Empty_Set))

Empty_Set.add(1)
Empty_Set.clear()
Empty_Set.add(77)
Empty_Set.add(77)
print(Empty_Set)
#Empty_Set.remove("ok") #ERROR

print(Empty_Set)


#.union()
print(Empty_Set.union(cars))

#.intersection()
print(Empty_Set.intersection(cars))