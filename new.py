# class Student:
#     def __init__(self):
#         self.name = 'harsha'
#         self.age = 22
#         self.addr= 'bengaluru'
#         self.quali = 'B.E'
#     def eat(self):
#         print(f'{self.name} is eating') 
#     def study(self):
#         print(f'{self.name} is studying')


# f1 = Student()
# print(f1)
# print(f1.name)
# print(f1.age)
# print(f1.addr)
# print(f1.quali)
# f1.eat()
# f1.study()

class Bike:
    def __init__(self):
        self.brand = 'yamaha'
        self.color = "Yellow"
        self.cost = 1000000
        self.cc = 2000
    def move(self):
        print('bike is moving')

b1 = Bike()
print(b1.brand)
print(b1.color)
print(b1.cost)
print(b1.cc)
b1.move()
