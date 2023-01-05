"""
MRO - Method resolution order

"""

"""
Multiple Level Inheritance
Grandparent --> Parent --> child
"""


class grandparent:
    # grandparent methods
    pass

class parent(grandparent):
    # grandparent methosd
    # parent methods
    pass

class Child(parent):
    # grandparent properties
    # parent properties
    # childe properties
    pass




# example

class SandWatch:
    def __init__(self):
        self.start_sand_watch()

    def start_sand_watch(self):
        print("sand watch started")




class Clock(SandWatch):
    """simulate thr clock"""

    def __init__(self,hours,minutes,seconds):
        super().__init__()
        self.set_clock(hours,minutes,seconds)

    def set_clock(self,hours,minutes,seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def time(self):
        return f"{self.hours}:{self.minutes}:{self.seconds}"

    def start_sand_watch(self):
        print("sand watch started in clock class")


class Calendar:
    """simulate calendar"""
    def __init__(self,d,m,y):
        super().__init__()
        self.set_calendar(d,m,y)

    def set_calendar(self,d,m,y):
        self.__d = d
        self.__m = m
        self.__y = y
    def date(self):
        return f"{self.__d}/ {self.__m}/ {self.__y}"

    def start_sand_watch(self):
        print("sand watch started in clock class")



class CalendarClock(Clock,Calendar):
    def __init__(self,h,m,s,d,mon,year):
        Clock.__init__(self,h,m,s)
        Calendar.__init__(self,d,mon,year)




# calendarClock

# calendar_clock = CalendarClock(12,1,20,13,25,2024)
#
# calendar_clock.start_sand_watch()



"""
IF WE HAVE THE SAME METHOD IN DIFFERENT CLASSES WHICHONE WILL BE EXECUTED ??
--->> IT WILL EXECUTE THE NEAREST ONE
THSI IS KNOWN AS METHOD RESOLUTION ORDER
"""

# TO PRINT THE MRO
# search order of a method in multiple inheritance mesh

for m in CalendarClock.__mro__:
    print(m)