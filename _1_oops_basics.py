class Penguin:

    # class attributes
    family = 'Sphenicidae'

    # instance attributes
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

# king = Penguin("king_penguin",4,'white')
# yellow_eyed = Penguin('yellow-eyed',1,'brown')

# print class attributes
# print('scientific family of {0} is {1}'.format(king.name,king.__class__.family))
# print('scientific family of {0} is {1}'.format(yellow_eyed.name,yellow_eyed.__class__.family))



# print instance attributes

# print('Age of {} is {} and its color is {} '.format(king.name,king.age,king.color))
# print('Age of {} is {} and its color is {} '.format(yellow_eyed.name,yellow_eyed.age,yellow_eyed.color))


# add methods to our penguin class

class Penguin:

    # class attributes
    family = 'Spheniscidae'

    # instance attributes

    def __init__(self,name,age,color):
        self.name =name
        self.age = age
        self.color = color


    # methods
    def swim(self,):
        return f'{self.name} can swim'

    def sing(self,can_sing=False):
        if can_sing:
            return f"{self.name} can sing"
        return f"{self.name} cannot sing"

    def dance(self,can_dance=False):
        if can_dance:
            return f"{self.name} can dance"
        return f"{self.name} cannot dance"


# create new penguin objects

# obj 1
# rockhopper = Penguin('rockhopper',4,'brown')

# lets see if rockhopper can swin
# print(rockhopper.swim())

# if he can sing
# print(rockhopper.sing(True))

# similar with dance method

# obj 2
# happy_feet = Penguin('happy feet',4,'angel')

# print(happy_feet.swim())
#
# print(happy_feet.sing(False))
#
# print(happy_feet.dance(True))






# <--------------------INHERITANCE---------------------------------------->
# Creating parent class

class  Bird:
    kingdom = "avianzae"

    def __init__(self):
        print("A bird is created")

    def whoiam(self):
        print("I am a Bird")

    def swim(self):
        print("Birds cannot swim")

    def fly(self):
        print('i can dly')


# now create child class and make it inherit parent class


class Owl(Bird):
    def __init__(self):
        super().__init__()          # this gets parent attrib in this class
        print('owl is created')

    # override the parens methods

    def whoiam(self):
        print("iam an owl")


    # owls can fly so no need to override fly method

    def swim(self):
        print("some owls can swim")

    # owls can see in the night
    # this method is only for child class owl

    def night_vision(self):
        print("owls have night vision")




# Midnight = Owl()
# #Midnight.swim()
# #Midnight.whoiam()
# Midnight.swim()
# Midnight.night_vision()




# -----------------------ENCAPSULATION----------------------------------#

# it means to hide the atttributes of the class
# The attributes are only accessible in class and not outside
# we use __ to hide attributes



#ex

class Telephone:
    def __init__(self):
        # private variable declaration
        self.__price = 1000

    def sell(self):
        print(f"The price of phone is {self.__price}")

    # setter
    def set_price(self,new_price):
        if new_price>=100:
            self.__price = new_price
        else:
            print("The price cannot be less than 100")

    # getter
    def get_price(self):
        print(self.__price)




# the __price cannot be accessed or modified outside of class
# getter and setter functions are used to modifiy private variables

# phone = Telephone()
# phone.sell()
# phone.__price = 5000
# phone.sell()

# even if we set phone.__price = 5000 the __price wont change
# instead an instance attibute phone.__price will be created with value 5000

# print(phone.__price)  # it is unrelated of the class variable

# use getter and setter to change private variables

# phone.set_price(8000)
# phone.sell()







#-------------------------POLYMORPHISM---------------------------------#

# modification of class attributes in child classes to print differnt resulst

# the same function can return differetn resulst based on objects

# basically overriding functions

