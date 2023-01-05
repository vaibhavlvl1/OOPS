"""
operator overloading
"""

class Point:
    "A point in coordinate axis"
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y


# create Two point objects

p1 = Point(2,5)
p2 = Point(-1,4)

print("----------before overloading")
print(p1)
# __str__() is same as print method



"""
define ouw own string represetnation  -- override __str__()  as operaroe overloading

"""



class Point:
    "A point in coordinate axis"
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    # overloading __str__() default method
    def __str__(self):
        return "this is a point of coordinates {} x {}".format(self.x,self.y)

print("-------after overloading")

p3 = Point(2,5)
print(p3)