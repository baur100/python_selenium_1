class Cup:
    def __init__(self, cups):
        self.cups = cups


    def cup_oz_convert(self):
        return 8 * self.cups


    def cup_tablespoon_convert(self):
        return 16 * self.cups


    def cup_gallon_convert(self):
        return 0.25 * self.cups
