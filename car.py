#Gas type
#1 Premium
#2 Regular
#3 Elite
#4 Diesel
class Car:
    def __init__(self, brand, model, gas_type):
        self.brand = brand
        self.model = model
        self.gas_type = gas_type

    def convert_gas(self):
        if self.gas_type == 1:
            return "Premium"
        elif self.gas_type == 2:
            return "Regular"
        elif self.gas_type == 3:
            return "Elite"
        else:
            return "Diesel"
1