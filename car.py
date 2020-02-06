# Gas type
#1 PREMIUM
#2 REGULAR
#3 ELITE
#4 DIESEL

class Car:
    def __init__(self, brand, model,gas_type):
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
        elif self.gas_type == 4:
            return "Diesel"