class Another:
    def __init__(self,num):
        self.num = num

    def f_prime(self):
        if self.num == 1:
            return False
        for i in range(2,self.num):
            if self.num % i == 0:
                return False
        return True

    def c_to_f(self):
        return (self.num - 32) * 5/9
