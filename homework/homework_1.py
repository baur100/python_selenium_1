# create class with 3 methods and write unit tests to it with a 3'A rule
# 0-1 = 60000
# 1-3 = 70000
# 3-5 = 85000
# > 5 = +20000/yearly

class Countries:
    def __init__(self, name, population, land_area, density):
        self.name = name
        self.population = population
        self.land_area = land_area
        self.density = density

    def county_pop(self):
        return self.name + self.population

    def area(self):
        return self.name == self.land_area

    def country_dens(self):
        return self.name + self.population + self.density

    def all_info(self):
        return self.name + self.population + self.land_area + self.density

    def loop(self):
        for country in self.name:
            if self.name == "Ukraine":
                return self.all_info()

    def overpopulation(self):
        if self.population > 150000000 and self.land_area < 9000000:
            return self.name + " is overpopulated"

