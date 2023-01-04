"""
Super Class
    child class 1
    child class 2

"""





class SuperClass():
    pass




class ChildClass1(SuperClass):
    pass


class ChildClass2(SuperClass):
    pass







#-----------------------------------------EXAMPLE___________________________#
# super class
class shapes:
    def __init__(self,color='red'):
        self.color = color


# childe class

class circle(shapes):
    def __init__(self,radius,color='green'):
        super().__init__(color)
        self.radius=radius

    def area(self):
        import math
        return math.pi*self.radius**2

# child class rectangel

class rectangle(shapes):
    def __init__(self,length=1.0,width=1.0,color ='orange'):
        super().__init__(color)
        self.width = width
        self.length = length

    def area(self):
        return self.width*self.length



# child class square

class square(shapes):
    def __init__(self,side=1.0,color='white'):
        super().__init__(color)
        self.side=side


    def area(self):
        return self.side**2



# create objects

sh = shapes('purple')
print(f"color of sh is {sh.color}")

# circle
ci = circle(5,'pink')
print(f"The radius of circle is {ci.radius} and color is {ci.color}")

# rectangel

re = rectangle(6,5)
print(f"rectangle with {re.length} length and {re.width} "
      f"width has area {re.area()} and its color is {re.color}")



'''
the 'object' class in python is the super class of all the classes

all  classes inherit from this 'object'class

ex class Super:      its same as class Super(object) 
generally its assumed and not written. No need 

'''

print(f"is shape class a sub class of object class ",isinstance(sh,object))

print(f"is square a subclass of shape class",issubclass(square,shapes))