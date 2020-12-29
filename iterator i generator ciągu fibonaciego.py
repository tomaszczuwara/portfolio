class fibonacci_iterator:
    def __init__(self, n):
        self.n = n
        self.generated_numbers = 0
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.generated_numbers == self.n:
            raise StopIteration
        self.generated_numbers += 1
        self.a, self.b = self.b, self.a + self.b
        return self.a


def fibocacci_generator(n):
    generator_numbers = 0
    a, b = 0, 1
    while generator_numbers != n:
        a, b = b, a + b
        generator_numbers += 1
        yield a

for i in fibocacci_generator(10):
    print(i)

for i in fibonacci_iterator(10):
    print(i)
print()

