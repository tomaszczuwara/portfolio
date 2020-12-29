class squere_iterator:
    def __init__(self, n):
        self.n = n
        self.generated_numbers = 0
        self.number = 0

    def __iter__(self): #metoda iter: musi zwrócić instatncję obiektu która zwróci metodę next i wyjątek
        return self

    def __next__(self):
        if self.generated_numbers == self.n:
            raise StopIteration
        self.generated_numbers += 1
        self.number = self.generated_numbers ** 2
        return self.number

def squere_generator(n):
    generator_numbers = 0
    while generator_numbers != n:
            generator_numbers += 1
            yield generator_numbers ** 2

for i in squere_generator(5):
    print(i)

for i in squere_iterator(5):
    print(i)
print()

