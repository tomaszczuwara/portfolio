class sum_iterator:
    def __init__(self, n):
        self.n = n
        self.generated_numbers = 0
        self.number = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.generated_numbers == self.n:
            raise StopIteration
        self.generated_numbers += 1
        self.number += self.generated_numbers
        return self.number

def sum_genrator(n):
    generator_numbers = 0
    number = 0
    while generator_numbers != n:
        generator_numbers += 1
        number += generator_numbers
        yield number

for i in sum_iterator(4):
    print(i)
print()
for i in sum_genrator(4):
    print(i)

# 1 -> 1
# 2 -> 1 + 2 = 3
# 3 ->  3 + 3 = 6
# 4 -> 6 + 4 = 10

