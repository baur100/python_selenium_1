class Tv:
    def __init__(self, size, processor, price):
        self.size = size
        self.processor = processor
        self.price = price

    def f_price(self):
        if self.price <= 2500:
            return "good choice"
        elif 2501 >= self.price <= 3500:
            return " wait for sale "
        elif 3501 <= self.price <= 20000:
            return "too expensive"
        else:
            return "don't buy"

    def f_size(self):
        if 1 <= self.size <= 55:
            return "a bigger size recommenced "
        elif 56 >= self.size <= 75:
            return "very good deal"
        elif 76 <= self.size <= 250:
            return "best deal"
        else:
            return "not possible"

    def f_processor(self):
        if self.processor == 2:
            return "too slow"
        elif self.processor == 4:
            return "a better one recommenced "
        elif 6 <= self.processor <=8:
            return "perfect"
        else:
            return "wrong data"



