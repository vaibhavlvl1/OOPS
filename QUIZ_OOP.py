"""
 [10 Questions] QUIZ - OOP
"""

# --------------------------------------------------------------------------------------#

# Q 1:
"""
Define a class named Student.
Student has two attributes:
* name (str)
* number (str)

Create two student objects out of this class.
The objects will be:
1- name: James Bond, number: 007
2- name: Klark Kent, number: 333

Print their names.

Hints:
* __init__

Exptected Output:
James Bond
Klark Kent
"""


# S 1:




# --------------------------------------------------------------------------------------#

# Q 2:
"""
The Student class you defined in Q1, has a new attribute.
This attribute is 'courses' and it will keep the list of courses, that the student takes.
Its type is list and it will initialize as an empty list.

There will be a method named 'enroll' to enroll the course.
The student will enroll the course, if it has not enrolled already.

Moreover, there will be a method named 'get_courses' which will return the course list.

Redefine the Student class based on these information.

Student data:
name: John Doe, number: 1111
courses: 
    * Python Hands-On
    * Machine Learning

Expected Output:
student.get_courses()  ->  ['Python Hands-On', 'Machine Learning']
"""


# S 2:




# --------------------------------------------------------------------------------------#

# Q 3:
"""
Define a class named 'Point'.
It will represent a point in x-y coordinate space.
And the docstring will be:
'it represents a point in (x,y) coordinates.'

Attributes: 
    * x (int) 
    * y (int)

Define __init__() for Point.
And it has a method named 'distance' which calculates the distance between two Points.
The first point is the current point (self) and the second will be the parameter.

Hints:
* to calculate distance (d):
    * get the difference between x values (x_diff)
    * get the difference between y values (y_diff)
    * d = math.sqrt(x_diff**2 + y_diff**2)
    
Expected Output:
p_1 -> (1, 7)
p_2 -> (4, 3)
dist = p_1.distance(p_2)
print(dist) ->  5.0
"""

# S 3:





# --------------------------------------------------------------------------------------#

# Q 4:
"""
Define a class named Rectangle.
It represents a rectangle on the X-Y coordinate axis.
And this is its docstring:
"This class represents a rectangle on (x,y) coordiante axis."

Rectangle has 4 attributes:
    * corner_1 (Point)
    * corner-2 (Point)
    * corner_3 (Point)
    * corner_4 (Point)

The type of these 4 corners are the Point class we defined in Q3.

Corner 1 and 2 are on the same line (side).
Corner 3 and 4 are on the same line (side).

This is how the corners look like:

1..............2
.              .
.              .
.              .
3..............4

Define the __init__() for Rectangle class.

It has methods to calculate its width and length.
    * width = distance between corner 1 and 2 -> calculate_width()
    * lenght = distance between corner 1 and 3 -> calculate_length()
    
Rectangle uses Point class to calculate these distances.

Finally, Rectangle has a method which returns its area.
The name of this method is 'area'.

Expected Output:
p_1 = Point(5, 8)
p_2 = Point(9, 8)
p_3 = Point(5, 2)
p_4 = Point(9, 2)

width = rect.width
length = rect.length
area = rect.area()

width: 4.0
length: 6.0
area: 24.0
"""


# S 4:




# --------------------------------------------------------------------------------------#

# Q 5:

"""
Define a class named BankAccount.
It has an attribute: balance (int)
And it has two methods:
    * withdraw -> removes money from balance
    * deposit -> adds money to balance

Both methods will update the balance and return the final balance.
The initial balance is 0. (__init__())

Finally there is method named 'display_balance' and it will print the current balance as:
'Balance: xxxxxx'

Expected Output:
account = BankAccount()
account.display_balance()
account.deposit(500)
account.display_balance()
account.withdraw(200)
account.display_balance()

Balance: 0
Balance: 500
Balance: 300
"""


# S 5:




# --------------------------------------------------------------------------------------#

# Q 6:
"""
Define a class named MinimumBankAccount.
This class will inherit from the BankAccount defined in Q5.
It will have an attribute as 'min_balance' to keep the minimum balance.
The value for min_balance will be defined while object instatiation. (__init__())

We wil check the min_balance when the user wants to withdraw:
* If after withdraw, the balance is less than min_balance
    * we will not let this withdraw
    * and we will return as: 'Sorry, you can not withdraw this amount.'

Finally modify the class so that it prints some meaningful data like:
print(MinimumBankAccount) -> 'This is MinimumBankAccount class'.

Hints:
* super()
* __str__  -> operator overloading
* do not implement withdraw in this class. 
  Super class (BankAccount) is already doing this.
  You should just check it here.

Expected Output:
min_account = MinimumBankAccount(100)
print(min_account)
min_account.deposit(500)
min_account.display_balance()
min_account.withdraw(200)
min_account.display_balance()
min_account.withdraw(300)
min_account.display_balance()

This is MinimumBankAccount class
Balance: 500
Balance: 300
Sorry, you can not withdraw this amount.
Balance: 300
"""


# S 6:




# --------------------------------------------------------------------------------------#

# Q 7:
"""
What is the result of print() functions below will?

class K:
    def a(self):
        return self.b()

    def b(self):
        return 'K'

class L(K):
    def b(self):
        return 'L'

k = K()
l = L()

print(k.b(), l.b())
print(k.a(), l.a())
"""

# S 7:





# --------------------------------------------------------------------------------------#

# Q 8:
"""
Define two classes as below:

Song:
The class for songs.
Each song has: 'name', 'artist', 'album' and 'song_number'.
'album' will be of type Album class.

Album:
The class for albums.
Each album has: 'name', 'artist', 'year' and 'songs'.
'songs' will be a list of Song class objects.
Album class has a method named 'add_song' to append a song to the 'songs' list.
It creates a song number while appending to the list.

Print the songs in the Album.

Expected Output:
album = Album('Yesterday and Today', 'The Beatles', 1966)
album.add_song('Yesterday')
album.add_song('Act Naturally')
album.add_song('What Goes On')

Yesterday
Act Naturally
What Goes On
"""


# S 8:




# --------------------------------------------------------------------------------------#

# Q 9:
"""
Define a class named Artist.
Each artist has 'name' and 'albums'.
'albums' is a list of type Album class we defined in Q8.

Methods: 
    * 'add_album(Album)' -> adds an album

Print all the songs of the artist.

Expected Output:
# Artist
beatles = Artist('The Beatles')

# Album
album_1 = Album('Yesterday and Today', 'The Beatles', 1966)
album_1.add_song('Yesterday')
album_1.add_song('Act Naturally')
beatles.add_album(album_1)

album_2 = Album('Let It Be', 'The Beatles', 1970)
album_2.add_song('Let It Be')
album_2.add_song('For You Blue')
beatles.add_album(album_2)


Yesterday
Act Naturally
Let It Be
For You Blue
"""


# S 9:




# --------------------------------------------------------------------------------------#

# Q 10:
"""
Overload the add (+) operator for Album class.
You will be able to add to Albums as:
Album + Album
And the result of this addition is the list of all songs in both classes.

If you do not overload the + operator and call as:
print(album_1 + album_2)
You will get an error:
TypeError: unsupported operand type(s) for +: 'Album' and 'Album'

Hints:
* __add__()  -> this is + operator method

Expected Output:
album_1 = Album('Yesterday and Today', 'The Beatles', 1966)
album_1.add_song('Yesterday')
album_1.add_song('Act Naturally')

album_2 = Album('Let It Be', 'The Beatles', 1970)
album_2.add_song('Let It Be')
album_2.add_song('For You Blue')

all_songs = album_1 + album_2


Yesterday
Act Naturally
Let It Be
For You Blue
"""


# S 10:




# --------------------------------------------------------------------------------------#