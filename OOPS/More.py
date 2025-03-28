# we are creating our own data type like < class = 'str'>

class Car:
    def __init__(self, model:str, year=2000):
        #Check the received arguements
        assert 2025 > year >= 2000 , f"I want car from 2000 to 2025 not {year}"


        # Assign to self object
        self.model = model
        self.year = year

        print("A car is created!")
        print(f"A model created > {model}")
    def price(self):  
        return self.year * 1000          #function inside class called methods

rollsRoyce = Car('ghost', 1000)
print(rollsRoyce.price())

BMW = Car('M4')
print(BMW.price())

print(type(rollsRoyce))
print(type(rollsRoyce.model))
print(type(rollsRoyce.price))