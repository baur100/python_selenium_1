# create class with 3 methods and write unit tests to it with a 3'A rule
# 0-1 = 60000
# 1-3 = 70000
# 3-5 = 85000
# > 5 = +20000/yearly

class EngSalary:
    def __init__(self, name, title, years, salary):
        self.title = title
        self.years = years
        self.salary = salary
        self.name = name

    def pay_scale(self):
        if self.years == "0-1":
            return 60000
        elif self.years == "1-3":
            return 70000
        elif self.years == "3-5":
            return 85000


    def senior(self):
        if self.years > 5:
            return self.salary + 20000

    def promotion(self):
        if self.years in self.title:
            return self.title == "Senior"
