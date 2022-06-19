class Clock:
    def __init__(self, hour, minute):
        self.hour = (hour + minute // 60) % 24
        self.minute = minute % 60
        

    def __repr__(self):
        return 'Clock({0}, {1})'.format(self.hour, self.minute)

    def __str__(self):
        return '{0:0>2}:{1:0>2}'.format(self.hour,self.minute)

    def __eq__(self, other):
        if self.hour == other.hour and self.minute == other.minute:
            return True
        else:
            return False

    def __add__(self, minutes):
        self.hour = self.hour + minutes // 60
        self.minute = self.minute + minutes % 60
        self.hour = (self.hour + self.minute // 60) % 24
        self.minute = self.minute % 60
        return '{0:0>2}:{1:0>2}'.format(self.hour,self.minute)

    def __sub__(self, minutes):
        self.hour = self.hour - minutes // 60
        self.minute = self.minute - minutes % 60
        self.hour = (self.hour + self.minute // 60) % 24
        self.minute = self.minute % 60
        return '{0:0>2}:{1:0>2}'.format(self.hour,self.minute)
