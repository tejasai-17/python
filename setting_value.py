class Date:
    def _init_(self):
        self.day = 0
        self.month = 0
        self.year = 0


d = Date()
d.day = 2
d.month = 8
d.year = 1991
print("day=", d.day)
print("month=", d.month)
print("year=", d.year)