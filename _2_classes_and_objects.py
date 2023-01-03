# defining a class
# docstring

class Car:
    """
    This is The Car Class
    """
    Brand = "BMW"

    def work(self):
        print('This car works')

# to call class attrib
#print(Car.Brand)

'''
dunder (double underscore attrib)
methods or attributes with two underscores prefixes
there are built in dunder methods
'''
# docstring of class
#print(Car.__doc__)

#get details of work method
# print(Car.work)

# call the work method  needs an object to be created
# object1 = Car()

# object1.work()

# above is same as
# Car.work(object1)



#ex
import math

class circle:
    def __init__(self,radius):
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def set_radius(self,new_radius):
        if new_radius >0:
            self.__radius = new_radius
        else:
            "radius must be positive"

    def perimeter(self):
        return math.pi * self.__radius*2


# create object

# circle1 = circle(10)
# print(circle1.get_radius())
# print(circle1.perimeter())
#
# circle1.set_radius(20)
# print(circle1.perimeter())




class Student:
    """
    Student database
    """
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade



# std = Student('jane doe',14,'7th grade')
# print(std.name,
#       std.age,
#       std.grade)

# --------------delete attributes from objects--------------------#
# obj.attrib
# del obj to delete to object itself
# del std.age
# age attributes deleted





