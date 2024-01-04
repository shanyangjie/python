import datetime


class TestClass:

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def sample(cls, date_diff=0):
        today = datetime.date.today()
        d=today + datetime.timedelta(days=date_diff)
        return cls(d.year, d.month, d.day)

a=TestClass.sample()
print(a.year,a.month,a.day)

b=TestClass.sample(5)
print(b.year,b.month,b.day)

c=TestClass(2025,1,29)
print(c.year,c.month,c.day)