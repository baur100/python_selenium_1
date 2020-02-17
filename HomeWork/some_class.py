class SomeClass:
    def __init__(self, number, string, another_number):
        self.number=number
        self.string=string
        self.another_number=another_number

    def check_odd_or_even_number(self):
        if self.number%2:
            return "Odd"
        else:
            return "Even"

    def sum_number_anotherNumber(self):
        return self.number+self.another_number

    def check_CapitalString(self):
        chk=False
        if self.string[0].isupper():
            chk=True
        return chk



