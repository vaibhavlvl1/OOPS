"""
multiple inheritence
A class can inherit from multiple classes
"""

class Main_1:
    pass
class Main_2:
    pass

class subclass(Main_2,Main_1):
    pass


#EX
# Clock and calender ---- calenderclock will inherit from both

class Clock:
    """simulate thr clock"""

    def __init__(self,hours,minutes,seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_clock(self,hours,minutes,seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def time(self):
        return f"{self.hours}:{self.minutes}:{self.seconds}"

# clock = Clock(0,0,0)
# print(clock.time())
# clock.set_clock(15,9,33)
# print(clock.time())


# calendar class
class Calendar:
    """simulate calendar"""
    def __init__(self,d,m,y):
        self.__d=d
        self.__m=m
        self.__y = y

    def set_calendar(self,d,m,y):
        self.__d = d
        self.__m = m
        self.__y = y
    def date(self):
        return f"{self.__d}/ {self.__m}/ {self.__y}"

# cal  = Calendar(11,12,2023)
# print(cal.date())


# create a multiple inheritance class

class CalendarClock(Clock,Calendar):
    def __init__(self,h,m,s,d,mon,year):
        Clock.__init__(self,h,m,s)
        Calendar.__init__(self,d,mon,year)


CalCock = CalendarClock(15,21,22,3,1,2023)

print(CalCock.time())
print(CalCock.date())

