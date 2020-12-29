niepodzielne = []

for x in range (1, 100):
    if x% 3 != 0:
        niepodzielne.append(x)
print(niepodzielne)

# listy
lst = range(1,101)
def niepodzielne_3 (lst):
    new_lst = []
    for elem in lst:
        if elem % 3 != 0:
            new_lst.append(elem)
    return new_lst

print(niepodzielne_3(lst))
"""
funkacja filter:
 Wbudowana funkcja filter, podobnie jak
dwie poprzednie również przyjmuje jako
swoje parametry funkcję oraz kolekcję.
Funkcja musi być jednoargumentowa.
● Jako wynik zwraca te elementy kolekcji, dla
których funkcja zwróciła True. Te dla których
funkcja zwróciła False zostały odfiltrowane.
● Na przykładzie obok funkcja odfiltrowuje
parzyste elementy kolekcji liczb całkowitych
z przedziału od jednego do stu.
● W efekcie zostały nam tylko liczby
nieparzyste.
"""
lst = range(1,101)
print(list(filter(lambda x: x % 3, lst)))

# idiomatyczne pythonowe - comprehation, najlepsze
print([x for x in lst if x % 3])

# modulo wyjaśnienie:
# 2/3 = 0 r. 2
# 3/3 = 1 r. 0
# 7/3 = 2 r. 1

# 2%3 = 2
# 3%3 = 0
# 7%3 = 1

