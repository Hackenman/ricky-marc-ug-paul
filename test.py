class Arithmetic(object):
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def add(self):
        return self.num1 + self.num2

    def multiply(self):
        return self.num1 * self.num2

    def mean(self):
        return (self.num1 + self.num2) / 2

    def describe(self):
        return print('Not yet')
