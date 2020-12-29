import re

#wersja moja

numer = input('Podaj numer telefonu w formacie 7XXXXXXXX lub 8XXXXXXXX lub 9XXXXXXXX\n')

if len(numer) == 9:
    if numer[0] == 7 or 8 or 9:
        print("Numer jest prawidłowy")
    else:
        print('numer zły')
else:
    print('nr niepoprawnej długości, popraw numer')
# wersja trenera

def is_number_correct(number):
    pattern = r"[7-9][0-9]{8}"
    return bool(re.fullmatch(pattern, numer))

numer = input('Podaj numer telefonu w formacie 7XXXXXXXX lub 8XXXXXXXX lub 9XXXXXXXX\n')
print(is_number_correct(numer))
