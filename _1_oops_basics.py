class Penguin:

    # class attributes
    family = 'Sphenicidae'

    # instance attributes
    def __init__(self,name,age,color):
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
        print("i cannot swim")

    def fly(self):
        print('i can dly')


# now create child class and make it inherit parent class


class Owl(Bird):
    def __init__(self):
        super().__init__()          # this gets parent attrib in this class
        print('owl is created')




Midnight = Owl()



