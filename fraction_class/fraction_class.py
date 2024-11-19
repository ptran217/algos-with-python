class Fraction:
    # constructor
    def __init__(self,top,bottom):
        common = gcd(top,bottom)
        self.num = top // common
        self.den = bottom // common


    # print override
    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    # add override
    def __add__(self, other):
        new_num = self.num*other.den + \
            self.den*other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    # sub override
    def __sub__(self, other):
        new_num = self.num*other.den - \
            self.den*other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    # override multiplication
    def __mul__(self, other):
        new_num = self.num*other.num
        new_den = self.den*other.den
        return Fraction(new_num, new_den)

    # override division
    def __truediv__(self, other):
        new_num = self.num*other.den
        new_den = self.den*other.num
        return Fraction(new_num, new_den)

    # deep equality
    def __eq__(self, other):
        first_num = self.num * other.den
        second_num = other.num * self.den
        return first_num == second_num

    def get_num(self):
        return self.num

    def get_den(self):
        return self.den

def gcd(m, n):
    while m % n != 0:
        old_m = m
        old_n = n
        m = old_n
        n = old_m % old_n
    return n

f_1 = Fraction(2,6)
f_2 = Fraction(1,2)

print(f_1 / f_2)