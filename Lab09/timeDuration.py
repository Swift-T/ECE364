class TimeSpan:
    def __init__(self,weeks=0,days=0,hours=0):
        self.weeks = weeks
        self.days = days
        self.hours = hours
        if type(self.weeks) is not int or type(self.days) is not int or type(self.hours) is not int:
            raise TypeError
        if self.weeks <0 or self.days <0 or self.hours<0:
            raise ValueError
        self.days += int(self.hours/24)
        self.weeks += int(self.days/7)
        self.hours %= 24
        self.days %= 7
    def __str__(self):
        h = str(self.hours) + 'H'
        d = str(self.days) + 'D'
        w = str(self.weeks) + 'W'
        if int(self.hours) < 10:
            h = '0' + h
        if int(self.weeks) < 10:
            w = '0' + w
        return w+' ' + d + ' ' + h
    def getTotalHours(self):
        return self.hours + self.days*24+self.weeks*7*24

    def __add__(self, other):
        if isinstance(other,self.__class__):
            return TimeSpan(self.weeks + other.weeks,self.days+other.days,self.hours+other.hours)
        else:
            raise TypeError
    def __mul__(self, other):
        if type(other) is not int:
            raise TypeError
        else:
            if(other == 0):
                raise ValueError
            else:
                return TimeSpan(self.weeks*other,self.days*other,self.hours*other)

    def __rmul__(self, other):
        if type(other) is not int:
            raise TypeError
        else:
            if(other == 0):
                raise ValueError
            else:
                return TimeSpan(self.weeks*other,self.days*other,self.hours*other)