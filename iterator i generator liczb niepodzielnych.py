# Zadanie 1
# Stwórz iterator i generator, które będą zwracały n liczb niepodzielnych
# przez m.
# np. dla n=10, m=3: [1, 2, 4, 5, 7, 8, 10, 11, 13, 14]

class indivisible_iterator: # iterator - trzeba stworzyć klasę

    def __init__(self, n, m):

        self.n = n
        self.m = m
        self.generated_numbers = 0 # ile wygenerowaliśmy
        self.number = 0 # liczbę od której zaczynamy iterację

    def __iter__(self):
        return self

    def __next__(self):
        self.number += 1
        if self.number == self.n:
            raise StopIteration
        if self.generated_numbers % self.m != 0: #generujemy tylko liczby niepodzielne przez m
            self.generated_numbers += 1
            return self.number
        return self.__next__()

def indivisible_generator(n, m):
    number = 1
    generated = 0
    while generated != n:
        if number % m > 0:
            yield number
            generated += 1
        number += 1

for i in indivisible_generator(10, 3):
    print(i)

for i in indivisible_iterator(10, 3):
    print(i)

