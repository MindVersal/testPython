import copy

print('Chapter 10')
print('Test Copy')

class Car:
    pass
car1 = Car()
car1.wheels = 4
car2 = Car()
car2.wheels = 3
print(car1.wheels)
car3 = copy.copy(car1)
car3.wheels = 6
print(car3.wheels)
print('THE END.')
