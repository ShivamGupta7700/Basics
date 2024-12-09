#__init__

class car():
    #default
    # def __init__(self):
    #     pass
    #parametor
    Origin = "Earth"
    def __init__(self, name, price): #attributes
        self.name = name 
        self.__price = price

    def greet(self):
        print(f"hello {self.name}")


carFirst = car("rolls royce", 7)
print(carFirst.name)
carFirst.greet()

carSecond = car("BMW M4", 1.54)
print(carSecond.name)  
print(carSecond.Origin)  
print(carSecond.__price)  #private attributes

